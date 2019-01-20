import os
from flask_testing import TestCase

from urlshortener import create_app, database
from urlshortener.models import Url

class TestUrlShortenerApp(TestCase):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = 'false'
    TESTING = True

    def create_app(self):
        os.environ['FLASK_SECRET_KEY'] = 'xJw<dYe]B]x%NK__UP?SnvPlU0ocH?y\'7OB#1J!6*~u.*^_O:bTsvn&SfRxmB^+'
        return create_app(self)

    def setUp(self):
        database.init_db()

    def tearDown(self):
        database.db.session.remove()
        database.db.drop_all()

    def test_app_runs(self):
        rv = self.client.get('/')
        self.assert200(rv)

    def test_404_page(self):
        rv = self.client.get('/foo/bar')
        self.assert404(rv)

    def test_index_route(self):
        rv = self.client.get('/')
        self.assertTemplateUsed('shortener/index.html')

    def test_index_route_with_urls(self):
        url = Url(url='https://www.google.com/', public=True, title='Google')
        database.db.session.add(url)
        database.db.session.commit()

        assert url in database.db.session

        rv = self.client.get('/')
        self.assertTemplateUsed('shortener/index.html')

    def test_create_route_missing_params(self):
        rv = self.client.post('/')
        self.assert400(rv)

    def test_create_route_missing_url(self):
        rv = self.client.post('/', data=dict(
            url=''
        ))
        self.assertRedirects(rv, '/')
        self.assertMessageFlashed('URL required')

    def test_create_route(self):
        rv = self.client.post('/', data=dict(
            url='https://www.google.com/',
            public='true'
        ))
        self.assertRedirects(rv, '/2/info')

    def test_info_route_404(self):
        rv = self.client.get('/2/info')
        self.assert404(rv)

    def test_info_route(self):
        url = Url(url='https://www.google.com/', public=True, title='Google')
        database.db.session.add(url)
        database.db.session.commit()

        assert url in database.db.session

        rv = self.client.get('/2/info')
        self.assert200(rv)
        self.assertTemplateUsed('shortener/info.html')

    def test_open_route_404(self):
        rv = self.client.get('/2')
        self.assert404(rv)

    def test_open_route(self):
        url = Url(url='https://www.google.com/', public=True, title='Google')
        database.db.session.add(url)
        database.db.session.commit()

        assert url in database.db.session

        rv = self.client.get('/2')
        self.assertRedirects(rv, 'https://www.google.com/')

    def test_about_route(self):
        rv = self.client.get('/info/about')
        self.assert200(rv)
        self.assertTemplateUsed('info/about.html')

    def test_privacy_route(self):
        rv = self.client.get('/legal/privacy')
        self.assert200(rv)
        self.assertTemplateUsed('legal/privacy.html')

    def test_terms_route(self):
        rv = self.client.get('/legal/terms')
        self.assert200(rv)
        self.assertTemplateUsed('legal/terms.html')
