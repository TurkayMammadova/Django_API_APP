from django import template
from Currency.models import CurrencyRate,Currency



register = template.Library()

# @register.filter
# def currency_rate_first(first_date):
#     currency_rate_first = CurrencyRate.objects.filter(date=first_date).first().rate
#     return currency_rate_first


@register.filter
def get_second_rate(code, second_date):

    second_rate = CurrencyRate.objects.filter(date=second_date, code=code).first().rate
    return second_rate

  
# @register.filter
# def currency_difference(first_date,second_date):
#     # rate_names = Currency.objects.all()
#     # for name in rate_names:
#         first_rate = CurrencyRate.objects.filter(date=first_date).first().rate
#         second_rate = CurrencyRate.objects.filter(date=second_date).first().rate

#         difference = 'fa-right-left'
#         if first_rate > second_rate:
#             difference = 'fa-arrow-down'
#         elif first_rate< second_rate:
#             difference = 'fa-arrow-up'

#         return difference

@register.filter
def currency_difference(code, args):
    date_list = args.split(',')
    first_date = date_list[0]
    second_date = date_list[1]
    first_rate = CurrencyRate.objects.filter(code=code, date=first_date).first().rate
    second_rate = CurrencyRate.objects.filter(code=code, date=second_date).first().rate
    difference = 'fa-right-left'
    if first_rate > second_rate:
        difference = 'fa-arrow-down'
    elif first_rate< second_rate:
        difference = 'fa-arrow-up'

    return difference