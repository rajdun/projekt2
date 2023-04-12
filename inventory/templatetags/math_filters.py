from django import template

register = template.Library()


@register.filter(name='mul')
def mul(value, arg):
    return value * arg


@register.filter
def round_value(value, param):
    return round(value, param)
