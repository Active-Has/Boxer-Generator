from unittest.mock import patch
from urllib import response
from flask import url_for
from flask_testing import TestCase
import requests_mock
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestHome(TestBase):
    def get_data(self):
        return {'boxer_api' : self.boxer_api, 'stamina_api' : self.stamina_api, 'strength_api' : self.strength_api, 'stats' : self.stats}
    
class TestResponse(TestBase):
    def test_response(self):
        with requests_mock.Mocker() as m:
            m.get('http://stamina-api:5000/get_boxer', text = 'Mike Tyson')
            m.get('http://stamina-api:5000/get_stamina', json=20)
            m.get('http://strength-api:5000/get_strength', json=20)
            m.post('http://merge-api:5000/post_stats', json={'name' : 'Mike Tyson', 'stamina_api' : 20, 'strength_api' : 20, 'stats' : 'Expert'})
        
            response = self.client.get(url_for('boxer'))
            self.assertEqual(response.status_code, 200)

    def test_response2(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)