# Created by Ayushi Rajendra Kumar at 10/25/2020

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
# Enter steps here
import datetime
import copy
import time
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

timeLog_data = [{
    "file_name": "test",
    "file_extension": "py",
    "detected_language": "python",
    "log_date": datetime.datetime.now().strftime("%Y-%m-%d"),
    "end_timestamp": time.time() + 500,
    "start_timestamp": time.time(),
    "api_token": "sample"
}]


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
        self.summary_url = reverse('timelog_summary_url')
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
        self.assertEqual(response.data["data"]["api_token"], user_Details.get('api_token'))
        self.assertNotEquals(user_Details.get('api_token'), None)

    def test_logtime(self):
        """
        Test behaviour of correct POST request for creating a user
        """
        user_url = f"{self.user_url}?type=signup"
        response = self.client.post(user_url, data=json.dumps(users_data1), content_type='application/json')
        user_Details = User.objects.get_user_from_username(username='ayushi2', password='123ayushi1')
        self.assertEqual(response.data["data"]["api_token"], user_Details.get('api_token'))
        timeLog_data[0]["api_token"] = user_Details.get('api_token')
        response = self.client.post(self.timelog_url, data=json.dumps(timeLog_data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_incorrect_get_signedup_user(self):
        """
        Test behaviour of incorrect POST request for logging in a user
        """
        user_url = f"{self.user_url}?type=login"
        response = self.client.post(f"{self.user_url}?type=signup", data=json.dumps(users_data1), content_type='application/json')
        incorrect_user = copy.deepcopy(users_data1)
        incorrect_user["password"] = "ayushi21"
        response = self.client.post(user_url, data=json.dumps(incorrect_user), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_invalid_user_signup_request(self):
        """
        Test behaviour of invalid POST request for logging in a user
        """
        user_url = f"{self.user_url}?type=signin"
        response = self.client.post(user_url, data=json.dumps(users_data1), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
