import imp
from django.urls import path
from .views import register_view, login_view

path('register/', register_view, name = 'register')