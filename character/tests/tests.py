import requests_mock
from flask_testing import TestCase
from application import app, routes


class TestBase(TestCase):
    def create_app(self):
        return app


class TestResponse(TestBase):
    def test_get_Two_Handed_Warrior(self):
        with requests_mock.Mocker() as m:
            m.get('http://archetype:5000/getarche', text='0')
            m.get('http://race:5000/getrace', text='High Elf')
            assert routes.getname()['name'] in ['Hyaril', 'Carene', 'Meanaami']