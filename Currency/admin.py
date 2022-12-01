from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from Currency.models import  Currency, CurrencyRate,History,Menu

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['name','code']
    list_filter = ['name','code']


admin.site.register(Menu)

@admin.register(CurrencyRate)
class CurrencyRateAdmin(admin.ModelAdmin):
    list_display = ['code', 'rate', 'date']
    list_filter = ['code', 'rate', 'date']

@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ['from_rate', 'to_rate', 'amount','currency_date','convert_date']

