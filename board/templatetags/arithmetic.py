from django import template
from datetime import datetime, timedelta

"""It's sometimes really handy to be able to do basic arithmetic in
Django templates.
"""


register = template.Library()


@register.filter
def sub(value, arg):
    return value - arg


@register.filter
def add(value, arg):
    return value + arg

@register.filter
def mul(value, arg):
    return value * arg

@register.filter
def ip(value):
    return value.replace(value.split(".")[0],"*",1)


@register.filter
def new(value):
    bftw = datetime.now() - timedelta(hours=12)
    valuedt = datetime(year=value.year, month=value.month, day=value.day, hour=value.hour, minute=value.minute, second=value.second)
    return True if datetime.now()< valuedt + timedelta(hours=12) else False 