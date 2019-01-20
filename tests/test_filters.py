import datetime
from urlshortener import filters

def test_format_datetime():
    now = datetime.datetime(2019, 1, 19, 19, 40, 30)
    assert filters._format_datetime(now) == '19.01.2019 19:40'

def test_format_datetime_medium():
    now = datetime.datetime(2019, 1, 19, 19, 40, 30)
    assert filters._format_datetime(now, 'full') == 'Jan 19, 2019, 7:40 PM'

def test_format_number_percent():
    assert filters._format_number(0.10, 'percent') == '10%'

def test_format_number_default():
    assert filters._format_number(1000) == '1,000'
