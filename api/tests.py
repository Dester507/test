import requests
from django.test import TestCase

from .models import Event


class EventPostTestCase(TestCase):
    def setUp(self):
        self.url = "http://127.0.0.1:8000/api/create-event/"

    def test_authentication_without_token(self):
        response = requests.post(self.url)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json().get("detail"), "Authentication credentials were not provided.")

    def test_authentication_with_token(self):
        header = {'Authorization': 'Token 96aa47a63fba548ec4d0de859f7afc4c8d7069e3'}
        response = requests.post(self.url, headers=header)
        self.assertEqual(response.status_code, 200)
    
    def test_create_exist_event(self):
        d = {"event_type": "match", "info": {"msg": "Hello"}, "timestamp": "2021-05-20T08:51:29"}
        header = {'Authorization': 'Token 96aa47a63fba548ec4d0de859f7afc4c8d7069e3'}
        response = requests.post(self.url, data=d, headers=header)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get("msg"), "You have already created an event")
        
    def test_create_event_with_bad_body(self):
        d = {"evnt_type": "match", "info": {"msg": "Hello"}, "timestamp": "123"}
        header = {'Authorization': 'Token 460d0b07a0afcfc6077c10f7e45e3818d47df265'}
        response = requests.post(self.url, data=d, headers=header)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get("msg"), "Bad Body")
