from django.db import models
from datetime import datetime
from django.utils import timezone
from simple_history.models import HistoricalRecords
from User.models import User

class Currency(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=4)
    status = models.CharField(max_length=50)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

   

class CurrencyRate(models.Model):
    code = models.CharField(max_length=4)
    date = models.DateField(default=timezone.now())
    rate = models.FloatField()

    def get_currency_name(self):
        currency_name = Currency.objects.filter(code=self.code).first().name
        return currency_name


    def __str__(self):
        return self.code
   
class History(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)   
    from_rate = models.CharField(max_length=100)
    to_rate = models.CharField(max_length=100)
    amount = models.FloatField()
    currency_date = models.DateField(default=timezone.now())
    convert_date = models.DateField(default=timezone.now())

    def __str__(self):
        return self.user.first_name


class Menu(models.Model):
    name = models.CharField(max_length=50)
    url_address = models.CharField(max_length=50)


    def __str__(self):
        return self.name
        
