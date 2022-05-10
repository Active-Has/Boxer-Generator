from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse2(TestBase):
    def test_strength(self):
        with patch('requests.get') as m:
            m.return_value.json = 20
            response = self.client.get(url_for('get_strength'))
            self.assertEqual(response.status_code, 200)