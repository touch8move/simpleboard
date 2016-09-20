from django import template

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