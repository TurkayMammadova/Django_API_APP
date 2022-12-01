from django import template
from math import ceil


register = template.Library()


@register.filter
def number_filter(numbers):
    float_num = float(numbers)
    if float_num>1000000000:
        number=(float_num/1000000000)
        new_num = round(number, 2)
        result = str(new_num)+'b'
    
    elif float_num>1000000:
        number=(float_num/1000000)
        new_num = round(number, 2)
        result = str(new_num)+ 'm'
    else:
        result=round(float_num,2)

    return result