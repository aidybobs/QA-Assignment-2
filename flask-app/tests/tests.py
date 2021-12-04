import app
from flask import url_for
from flask_testing import TestCase
import requests_mock
import requests


class TestBase(TestCase):
    def create_app(self):
        app.app.config.update(
            SQLALCHEMY_DATAVBASE_URI='sqlite:///test.db',
            DEBUG=True,
            SECRET_KEY='sjdahs'
        )
        return app.app


class TestResponse(TestBase):
    def test_home(self):
        response = self.client.get(url_for('generate'))
        self.assertEquals(response.status_code, 200)
        self.assertIn(b'Skyrim', response.data)

    def test_new(self):
        with requests_mock.Mocker() as m:
            m.get('http://character:5000/getchar', json={
                'name': 'John',
                'race': 'Human',
                'arche': 'Hunter'
            })
            assert requests.get('http://character:5000/getchar').json() == {
                'name': 'John',
                'race': 'Human',
                'arche': 'Hunter'
            }
