import imp
from django.urls import path
from .views import register, home, login


urlpatterns = [
    path('register/', register, name = 'register'),
    path('home/', home, name = 'home'),
    path('login/', login, name = 'login'),
    

]