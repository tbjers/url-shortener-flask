import datetime
from flask_testing import TestCase
from urlshortener import filters

from urlshortener import create_app

class TestFilters(TestCase):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = 'false'
    TESTING = True

    def create_app(self):
        return create_app(self)

    def test_format_datetime(self):
        now = datetime.datetime(2019, 1, 19, 19, 40, 30)
        assert filters._format_datetime(now) == '19.01.2019 19:40'

    def test_format_datetime_medium(self):
        now = datetime.datetime(2019, 1, 19, 19, 40, 30)
        assert filters._format_datetime(now, 'full') == 'Jan 19, 2019, 7:40 PM'

    def test_format_number_percent(self):
        assert filters._format_number(0.10, 'percent') == '10%'

    def test_format_number_default(self):
        assert filters._format_number(1000) == '1,000'
