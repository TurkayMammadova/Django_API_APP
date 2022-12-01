from django.urls import path
from .views import *


# app_name = 'currency'
urlpatterns = [
    path('', get_index, name = 'home'),
    path('todayrate', get_today_rates, name = 'todayrate'),
    path('comparerate',compare_two_rates, name = 'comparerate'),
    path('singlerate', get_single_rate, name = 'singlerate'),
    path('conversion', conversion_rates, name = 'conversion'),
    path('conversion_api', conversion_api, name = 'conversion_api'),
    path('setname', addRatesNames, name = 'setname'),
    path('addrates', addRatess, name = 'addrates'),
    path('getrates', get_rates, name='getrates')
]
