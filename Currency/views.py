from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import json
import time
import requests
import xmltodict
from datetime import datetime,timedelta
from django.utils import timezone
from Currency.models import CurrencyRate , Currency, History, Menu
from math import ceil



def get_index(request):
    return redirect('/todayrate')


def addRatesNames(request):
    today = datetime.now()
    date = today.strftime("%d.%m.%Y")
    currency = requests.get(f'https://www.cbar.az/currencies/{date}.xml', verify=False)
    currency_dict=xmltodict.parse(currency.content)
    currency_list = currency_dict['ValCurs']['ValType'][1]['Valute'] 
  
    for currency1 in currency_list:
        name = currency1['Name'] 
        code=currency1['@Code']
        status = 'any'
        currency = Currency( name=name,code=code, status=status)
        currency.save()
        

    return HttpResponse("ok")


def addRatess(input_date):
    date_str = datetime.strptime(input_date,"%Y-%m-%d")
    date = date_str.strftime('%d.%m.%Y')

    # date_list = input_date.split('-')
    # date = f'{date_list[2]}.{date_list[1]}.{date_list[0]}'
    currency = requests.get(f'https://www.cbar.az/currencies/{date}.xml',verify=False)
    currency_dict=xmltodict.parse(currency.content)
    currency_list = currency_dict['ValCurs']['ValType'][1]['Valute'] 
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print(currency_list )
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    

    for currency1 in currency_list:
        code = currency1['@Code']
        rate = currency1['Value']
        currency = CurrencyRate(code=code, rate=rate, date=input_date)
        currency.save()
    
    return 0

    

def get_rates(request):

    rate_list = []
    today = datetime.now()
    date = today.strftime("%Y-%m-%d")
    if request.method=='POST':
        date = request.POST['date']
    rate_names = Currency.objects.all()
    currencies = CurrencyRate.objects.filter(date=date)
    if not len(currencies):
        addRatess(date)
    # for name in rate_names:
    #     rate = CurrencyRate.objects.filter(date=date, code=name.code).first()
    #     single_rate = {
    #         'code': name.code,
    #         'rate': rate.rate
    #     }
    #     rate_list.append(single_rate)

    context = {
        'currency_list': CurrencyRate.objects.filter(date=date),
        'date': date,
    
    }

    return render(request, "currency/get-rates.html", context)


def conversion_rates(request):
    # new_name_list=[]
    # new_code_list = []
    name_list = Currency.objects.all()
    # old_code_list = CurrencyRate.objects.all()
    # for name in old_name_list:
    #     new_name={
    #         'name' : name.name,
    #         'code' : name.code,
            
    #     }
    #     new_name_list.append(new_name)
    # new_name_list.append({'name':'1 Azerbaycan manati', 'code':'AZN'})
    # for code in old_code_list:
    #     new_code={
    #         'code':code.code, 
    #     }
    #     new_code_list.append(new_code)
    # new_code_list.append({'code':'AZN'})   
    # print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    # print(new_name_list)
    # print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    result = 1.0

    if request.method == 'POST':
        from_currency = request.POST['from_currency']
        print('######################################')
        print(from_currency)
        print('######################################')

        to_currency = request.POST['to_currency']
        amount = request.POST['amount']
        input_date = request.POST['date']

        
        currencies = CurrencyRate.objects.filter(date=input_date)
        if not len(currencies):
            addRatess(input_date)
        
        from_cur_code = Currency.objects.filter(name=from_currency).first().code
        from_rate = CurrencyRate.objects.filter(date=input_date, code=from_cur_code).first().rate

        to_cur_code = Currency.objects.filter(name=to_currency).first().code
        to_rate = CurrencyRate.objects.filter(date=input_date, code=to_cur_code).first().rate
    

        result_ = (float(amount)*float(from_rate))/float(to_rate)
        result = ceil(result_ * 100) / 100.0

        # if to_cur_code =='AZN':
        #     from_cur_code = Currency.objects.filter(name=from_currency).first().code
        #     from_rate = CurrencyRate.objects.filter(date=input_date, code=from_cur_code).first().rate
            
        # result_ = (float(amount)*float(from_rate))
        # result = ceil(result_ * 100) / 100.0



        # user = request.user
        # from_rate = from_currency
        # to_rate = to_currency
        # currency_date = str_date
        # amount = amount
        # resp = History(user=user,from_rate=from_rate, to_rate=to_rate,currency_date=currency_date,amount=amount)
        # resp.save()
        
        # from_rate = CurrencyRate.objects.filter(name=from_currency, date=date).first()
        # to_rate = CurrencyRate.objects.filter(name=to_currency, date=date).first()

    context = {
        'name_list' : name_list,
        'result': result,
        # 'navbar': Menu.objects.all()
    }

    return render(request,'currency/conversion-rates.html',context)


def conversion_api(request):
    from_currency = request.GET['from_currency']
    to_currency = request.GET['to_currency']
    amount = request.GET['amount']
    input_date = request.GET['date']

    currencies = CurrencyRate.objects.filter(date=input_date)
    if not len(currencies):
        addRatess(input_date)

    from_rate = CurrencyRate.objects.filter(date=input_date, code=from_currency).first().rate if from_currency != "AZN" else 1.0
    to_rate = CurrencyRate.objects.filter(date=input_date, code=to_currency).first().rate if to_currency != "AZN" else 1.0

    result_ = (float(amount)*float(from_rate))/float(to_rate)
    result = ceil(result_ * 100) / 100.0

    data = {
        'result': result
    }

    return JsonResponse(data)


def get_today_rates(request):
    rate_list = []
    today = datetime.now()
    date = today.strftime("%Y-%m-%d")
    currencies = CurrencyRate.objects.filter(date=date)
    if not len(currencies):
        addRatess(date)

    context = {
        'currency_list': currencies,
        'date': date,
        
    }

    return render(request, "currency/today-rates.html", context)

  

def get_rates_by_date(request):
    currency_dates = []
    today = datetime.now()
    date = today.strftime("%d.%m.%Y")
    resp = requests.get(f'https://www.cbar.az/currencies/{date}.xml',verify=False)
    currency_dict=xmltodict.parse(resp.content)
    currency_list = currency_dict['ValCurs']['ValType'][1]['Valute'] 
    for currency in currency_list:
        currency_data = {
            'code': currency['@Code'],
            'rate': currency['Value']
        }
        currency_dates.append(currency_data)
        print('%%%%%%%%%%%%%%%%%%%%%%')
        print(currency_dates)
       
    context = {
        'currency_list': currency_list,
        # 'navbar': Menu.objects.all()
    }
    return render(request, "currency/rates-by-date.html", context)



def generate_compare_list(first_date, second_date):
    compare_list = []
    rate_names = Currency.objects.all()
    currency_first_list = CurrencyRate.objects.filter(date = first_date)
    currency_second_list = CurrencyRate.objects.filter(date = second_date)
    if not len(currency_first_list):
        addRatess(first_date)
    if not len(currency_second_list):
        addRatess(second_date)   
    for name in rate_names:
        first_rate = CurrencyRate.objects.filter(date=first_date, code=name.code).first()
        second_rate = CurrencyRate.objects.filter(date=second_date, code=name.code).first()

        difference = 'fa-right-left'
        if first_rate.rate > second_rate.rate:
            difference = 'fa-arrow-down'
        elif first_rate.rate < second_rate.rate:
            difference = 'fa-arrow-up'
        
        rate_name = {
            'name': name.name,
            'code': name.code,
            'first_rate':first_rate.rate,
            'second_rate':second_rate.rate,
            'difference' : difference,
            # 'navbar': Menu.objects.all()
        }
        compare_list.append(rate_name)

    return compare_list

def compare_two_rates(request):
    message = "The input element"
    yesterday=datetime.now()-timedelta(days=1)
    
    first_date = yesterday.strftime("%Y-%m-%d")
    second_date = datetime.now().strftime("%Y-%m-%d")

    if request.method == 'POST':
        message = f'{first_date} ve {second_date} tarixleri ucun valyuta mezennesi'
        first_input = request.POST['first_date']
        first_date = datetime.strptime(first_input,"%Y-%m-%d")
        second_input = request.POST['second_date']
        second_date = datetime.strptime(second_input,"%Y-%m-%d")

    currency_first_list = CurrencyRate.objects.filter(date = first_date)
    currency_second_list = CurrencyRate.objects.filter(date = second_date)
    if not len(currency_first_list):
        addRatess(first_date)
    if not len(currency_second_list):
        addRatess(second_date)   
           
    context = {
        'currency_list':currency_first_list,
        'msj':message,
        'first_date': first_date, 
        'second_date': second_date,
        'both_dates': f'{first_date},{second_date}'
        # 'navbar': Menu.objects.all()
    }
    
    return render(request, "currency/compare-rates.html", context)


def get_single_rate(request):
    # code_list = []
    # message = "The input element"

    date = datetime.now()
    input_date = date.strftime("%Y-%m-%d")
    code = ''
    rate = ''
    currency_list = CurrencyRate.objects.filter(date = input_date)
    if request.method == 'POST':
        date = request.POST['date']
        print("************************************")
        print(input_date)
        print("************************************")
        code = request.POST['code']
        input_date = datetime.strptime(date,"%Y-%m-%d")
        # message = f'{date} tarixinde olan {code} ucun valyuta mezennesi'
        currency_list = CurrencyRate.objects.filter(date=input_date)
        if not len(currency_list):
            addRatess(input_date)
        for currency in currency_list:
            if code == currency.code:
                rate = currency.rate
                
    currency_data = {

        'code': code,
        'rate': rate,
        'date' : input_date,
        'currency_list':currency_list,
        # 'navbar': Menu.objects.all()
    }
            


    return render (request, 'currency/single-rate.html', currency_data)


