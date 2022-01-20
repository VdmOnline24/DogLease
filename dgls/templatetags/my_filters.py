from django import template
from datetime import date, datetime

register = template.Library()

@register.filter(name='checkcolor')
def checkcolor(value):
    return 'a'

@register.filter(name='days_color')
def days_color(value):
    if isinstance(value, date):
        delta = value - date.today()
        if delta.days < 90:
            return 'table-danger'
        elif delta.days < 180:
            return 'table-warning'
        else:
            return 'table-light'

    else:
        return 'table-secondary'