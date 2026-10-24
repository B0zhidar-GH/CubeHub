from django import template

register = template.Library()

@register.filter
def seconds(value):
    try:
        return f'{float(value):.2f} seconds'
    except (TypeError, ValueError):
        return value