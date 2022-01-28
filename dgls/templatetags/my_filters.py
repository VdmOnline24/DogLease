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

@register.filter(name='drive_color')
def drive_color(value):
    if isinstance(value, int):

        if value > 30000:
            return 'table-danger'
        elif value > 20000:
            return 'table-warning'
        else:
            return 'table-light'

    else:
        return 'table-secondary'