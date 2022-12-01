
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import requests
import xmltodict
from .models import Symbol



def bitcoin_data(request):
    result_list = []
    symbol_list = []
    name_list = Symbol.objects.all()
    for symbol in name_list:
        symbol_list.append(symbol.name)
    api_response = requests.get("http://api.coincap.io/v2/assets")
    resp_json = api_response.json()
    coin_list = resp_json['data']

    i = 0
    symbol_check_increment = 0
    while symbol_check_increment < len(symbol_list):
        if coin_list[i]['symbol'] in symbol_list:       
            print("\n\n\n#########################\n\n\n")
            print(i)
            print(coin_list[i]['symbol'])
            single_coin = {
                'rank' : coin_list[i]['rank'],
                'name' : coin_list[i]['name'],
                'symbol': coin_list[i]['symbol'],
                'image': coin_list[i]['id'],
                'priceUsd' : coin_list[i]['priceUsd'],
                'marketCapUsd': coin_list[i]['marketCapUsd'],
                'vwap24Hr': coin_list[i]['vwap24Hr'],
                'supply':coin_list[i]['supply'],
                'volumeUsd24Hr': coin_list[i]['volumeUsd24Hr'],
                
            }  
            result_list.append(single_coin)

            symbol_check_increment+=1


        i += 1

    context={
        "coin_list":result_list
    }
        
    return render(request, "bitcoin/bitcoin.html", context)

   


