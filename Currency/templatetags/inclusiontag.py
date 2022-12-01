from django import template
from Currency.models import Menu

register=template.Library()

@register.inclusion_tag("navbar.html", takes_context=True)
def show_nav_bar(context):
    content = {
        'navbar': Menu.objects.all()
    }
    return content


