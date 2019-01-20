from datetime import timedelta, datetime
from flask_babel import format_datetime, format_percent, format_number, format_decimal, format_timedelta

def _format_datetime(value, format='medium'):
    if format == 'full':
        format="LLL dd, YYYY, h:mm a"
    elif format == 'medium':
        format="dd.MM.y HH:mm"
    return format_datetime(value, format)

def _format_number(value, format='number'):
    if format == 'decimal':
        return format_decimal(value)
    elif format == 'percent':
        return format_percent(value)
    return format_number(value)

def _format_relative_date(value):
    delta = value - datetime.today()
    return format_timedelta(timedelta(days=delta.days, seconds=delta.seconds), add_direction=True)

def init_filters(app):
    app.jinja_env.filters['datetime'] = _format_datetime
    app.jinja_env.filters['number'] = _format_number
    app.jinja_env.filters['relative'] = _format_relative_date
