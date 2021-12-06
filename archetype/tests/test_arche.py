from flask import url_for
from flask_testing import TestCase
import app


class TestBase(TestCase):
    def create_app(self):
        return app.app


class TestResponse(TestBase):
    def test_random(self):
        response = self.client.get(url_for('getarche'))
        self.assertEqual(response.status_code, 200)
