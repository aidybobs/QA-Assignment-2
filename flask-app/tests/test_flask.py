from application import app, db
from application.models import Characters
from flask import url_for
from flask_testing import TestCase
import requests_mock
import requests


class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI='sqlite:///test.db',
            DEBUG=True,
        )
        return app

    def setUp(self):
        db.create_all()
        sampleemp = Characters(name='James', race='Human', archetype='Warrior')
        db.session.add(sampleemp)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestResponse(TestBase):
    def test_home(self):
        response = self.client.get(url_for('generate'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'James', response.data)
        self.assertIn(b'Human', response.data)

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
