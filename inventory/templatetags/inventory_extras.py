from .. import decorators
from django import template

register = template.Library()


@register.filter
def can_manage_inventory(user):
    return decorators.can_manage_inventory(user)
