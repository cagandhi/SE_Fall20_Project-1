# Created by Ayushi Rajendra Kumar at 10/25/2020

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
# Enter steps here
import datetime

from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from rest_framework.utils import json
from ..models import User

users_data = {
    "log_user_id": 1223,
    "username": "ayushi2",
    "password": "123ayushi1",
    "api_token": "1234abcd"

}

users_data1 = {
    "username": "ayushi2",
    "password": "123ayushi1"

}

timeLog_data = {
    "log_file_time_id": 22,
    "file_name": "test",
    "file_extension": "py",
    "detected_language": "python",
    "log_date": str(datetime.date),
    "log_timestamp": str(datetime.datetime.now() + datetime.timedelta(hours=2)),
    "created_at": str(datetime.datetime.now()),
    "modified_at": str(datetime.datetime.now() + datetime.timedelta(hours=2))
}


class TestPostViews(TestCase):
    """
    Tests to verify the functioning of all the POST requests in bot_server/api
    """

    def setUp(self):
        """
        Test setup for each test in this class. It is done for each of the tests
        """
        self.client = Client()
        self.user_url = reverse('user_endpoint')
        self.timelog_url = reverse('timelog_url')
        # User.objects.create_user(users_data)

    def test_user(self):
        """
        Test behaviour of correct POST request for creating a user
        """
        user_url = f"{self.user_url}?type=signup"
        response = self.client.post(user_url, data=json.dumps(users_data1), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user_url = f"{self.user_url}?type=login"
        response = self.client.post(user_url, data=json.dumps(users_data1), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user_Details = User.objects.get_user_from_username(username='ayushi2', password='123ayushi1')
        self.assertEqual(user_Details.get('username'), users_data['username'])
        self.assertEqual(user_Details.get('password'), users_data['password'])
        self.assertNotEquals(user_Details.get('api_token'), None)

    def test_logtime(self):
        """
                Test behaviour of correct POST request for creating a user
                """
        response = self.client.post(self.timelog_url, data=json.dumps(timeLog_data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
