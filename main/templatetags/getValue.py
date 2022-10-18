import re
from django import template
from django.conf import settings

numeric_test = re.compile("^\d+$")
register = template.Library()

@register.filter
def return_item(l, i):
    try:
        return l[i]
    except:
        return None

def add(l, i):
    return l+i