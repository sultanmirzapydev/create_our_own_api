from django import template

register = template.Library()

@register.filter(name="check_str")
def check_str(val):
    return type(val)


