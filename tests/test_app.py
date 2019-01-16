import os
import unittest

from urlshortener import create_app, database

class UrlShortenerTests(unittest.TestCase):
    def setUp(self):
        os.environ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        os.environ['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'false'

        self.app = create_app()

        self.ctx = self.app.app_context()
        self.ctx.push()

        try:
            database.init_app(self.app)
            database.init_db()
        except Exception as ex:
            print(ex)
            self.fail('exception raised in init_app and init_db')

        self.client = self.app.test_client()

    def tearDown(self):
        self.ctx.pop()

    def test_app_runs(self):
        rv = self.client.get('/')
        self.assertEqual(rv.status, '200 OK')
