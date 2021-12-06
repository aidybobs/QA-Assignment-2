import requests_mock
from flask_testing import TestCase
from flask import url_for
from application import app


class TestBase(TestCase):
    def create_app(self):
        return app.app


class TestResponse(TestBase):
    def test_HE_Two_Handed_Warrior(self):
        with requests_mock.Mocker() as m:
            m.get('http://archetype:5000/getarche', text='0')
            m.get('http://race:5000/getrace', text='High Elf')
            response = self.client.post(url_for('getname'))
            self.assertIn(b'["Hyaril","Carene","Meanaami"]', response.data)
