from django.urls import path
from .views import bitcoin_data

# app_name = 'currency'
urlpatterns = [
    path('bitcoin',bitcoin_data, name = 'bitcoin'),
 

]