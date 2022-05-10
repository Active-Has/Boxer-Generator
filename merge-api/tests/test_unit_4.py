from unittest.mock import patch
import requests_mock
from flask import url_for, Response
from flask_testing import TestCase
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_get_stats(self):
        name = "Mike Tyson"
        stats1 = 20
        stats = 20
        fighter_level = "Expert"
        response = self.client.post(url_for('get_stats'), json={'name' : name, 'stamina_api' : stats1, 'strength_api' : stats, 'Expert' : fighter_level})
        self.assertEqual(response.status_code, 200)
    
    def test_get_stats1(self):
        name = "Floyd Mayweather"
        stats1 = 10
        stats = 20
        fighter_level = "Advanced"
        response = self.client.post(url_for('get_stats'), json={'name' : name, 'stamina_api' : stats1, 'strength_api' : stats, 'Expert' : fighter_level})
        self.assertEqual(response.status_code, 200)

    def test_get_stats2(self):
        name =  "Muhammad Ali"
        stats1 = 10
        stats = 10
        fighter_level = "Intermediate"
        response = self.client.post(url_for('get_stats'), json={'name' : name, 'stamina_api' : stats1, 'strength_api' : stats, 'Expert' : fighter_level})
        self.assertEqual(response.status_code, 200)
    
    def test_get_stats3(self):
        name = "Manny Pacquiao"
        stats1 = 5
        stats = 5
        fighter_level = "Beginner"
        response = self.client.post(url_for('get_stats'), json={'name' : name, 'stamina_api' : stats1, 'strength_api' : stats, 'Expert' : fighter_level})
        self.assertEqual(response.status_code, 200)
    
    def test_get_stats4(self):
        name = "Gennady Golovkin"
        stats1 = 50
        stats = 20
        fighter_level = "Professional"
        response = self.client.post(url_for('get_stats'), json={'name' : name, 'stamina_api' : stats1, 'strength_api' : stats, 'Expert' : fighter_level})
        self.assertEqual(response.status_code, 200)

    def test_get_stats5(self):
        name = "Mike Tyson"
        stats1 = 40
        stats = 40
        fighter_level = "World Class"
        response = self.client.post(url_for('get_stats'), json={'name' : name, 'stamina_api' : stats1, 'strength_api' : stats, 'Expert' : fighter_level})
        self.assertEqual(response.status_code, 200)

    def test_get_stats6(self):
        name = "Floyd Mayweather"
        stats1 = 45
        stats = 50
        fighter_level = "Legendary"
        response = self.client.post(url_for('get_stats'), json={'name' : name, 'stamina_api' : stats1, 'strength_api' : stats, 'Expert' : fighter_level})
        self.assertEqual(response.status_code, 200)

    def test_get_stats7(self):
        name = "Muhammad Ali"
        stats1 = 4
        stats = 4
        fighter_level = "Beginner"
        response = self.client.post(url_for('get_stats'), json={'name' : name, 'stamina_api' : stats1, 'strength_api' : stats, 'Expert' : fighter_level})
        self.assertEqual(response.status_code, 200)
    
    def test_get_stats8(self):
        name = "Manny Pacquiao"
        stats1 = 49
        stats = 49
        fighter_level = "Legendary"
        response = self.client.post(url_for('get_stats'), json={'name' : name, 'stamina_api' : stats1, 'strength_api' : stats, 'Expert' : fighter_level})
        self.assertEqual(response.status_code, 200)

