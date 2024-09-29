from django import template
from django.conf import settings as SETTINGS

register = template.Library()


# settings value
@register.simple_tag
def settings(name):
    return getattr(SETTINGS, name, "")
