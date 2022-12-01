from django import template
from Currency.models import Currency


register = template.Library()

@register.filter
def get_currency_name(code):
    currency_name = Currency.objects.filter(code=code).first().name
    return currency_name

  