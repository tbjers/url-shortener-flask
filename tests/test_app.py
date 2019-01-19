import os

from urlshortener import create_app, database

class TestUrlShortenerApp(object):
    def setup_class(cls):
        os.environ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        os.environ['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'false'

        cls.app = create_app()

        cls.ctx = cls.app.app_context()
        cls.ctx.push()

        database.init_app(cls.app)
        database.init_db()

        cls.client = cls.app.test_client()

    def teardown_class(cls):
        cls.ctx.pop()

    def test_app_runs(self):
        rv = self.client.get('/')
        assert rv.status == '200 OK'
