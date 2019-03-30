from django import template
import re

register = template.Library()

@register.filter
def cut_img(value):
    return re.sub(r'<img[^>]+>', '', value)