from babel.dates import format_datetime

def _format_datetime(value, format='medium'):
    if format == 'full':
        format="LLL dd, YYYY, h:mm a"
    elif format == 'medium':
        format="dd.MM.y HH:mm"
    return format_datetime(value, format)

def init_filters(app):
    app.jinja_env.filters['datetime'] = _format_datetime
