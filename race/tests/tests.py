import app
from flask_testing import TestCase
from flask import url_for


class TestBase(TestCase):
    def create_app(self):
        return app.app


class TestResponse(TestBase):
    def test_random(self):
        response = self.client.get(url_for('getrace'))
        self.assertEqual(response.status_code, 200)
