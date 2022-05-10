from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_boxer(self):
        with patch('requests.get') as m:
            m.return_value.text = "Mike Tyson"
            response = self.client.get(url_for('get_boxer'))
            self.assertEqual(response.status_code, 200)

class TestResponse2(TestBase):
    def test_stamina(self):
        with patch('requests.get') as m:
            m.return_value.json = 20
            response = self.client.get(url_for('get_stamina'))
            self.assertEqual(response.status_code, 200)