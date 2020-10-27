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
    "log_date": "2020-10-27",
    "end_timestamp": time.time() + 500,
    "start_timestamp": time.time(),
    "api_token": "sample"
}]


class TestPostViews(TestCase):
    """
    Tests to verify the functioning of all the POST requests in codetime_server/codetime
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


class TestGetViews(TestCase):
    """
    Tests to verify the functioning of all the GET requests in codetime_server/codetime
    """

    def setUp(self):
        """
        Test setup for each test in this class. It is done for each of the tests
        """
        self.client = Client()
        self.user_url = reverse('user_endpoint')
        self.timelog_url = reverse('timelog_url')
        self.summary_url = reverse('timelog_summary_url')
        user_url = f"{self.user_url}?type=signup"
        self.client.post(user_url, data=json.dumps(users_data1), content_type='application/json')
        user_Details = User.objects.get_user_from_username(username='ayushi2', password='123ayushi1')
        timeLog_data[0]["api_token"] = user_Details.get('api_token')
        self.client.post(self.timelog_url, data=json.dumps(timeLog_data), content_type='application/json')

    def test_get_summary_extension_api(self):
        """
        Test behaviour of GET request for getting summary by file extension
        """
        summary_url = f"{self.summary_url}?api_token={timeLog_data[0]['api_token']}&type=extension"
        response = self.client.get(summary_url, content_type='application/json')
        self.assertEqual(response.data['data'][0]['language'], timeLog_data[0]['file_extension'])
        self.assertEqual(response.data['data'][0]['count'], 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_summary_weekday_api(self):
        """
        Test behaviour of GET request for getting summary by weekdays
        """
        summary_url = f"{self.summary_url}?api_token={timeLog_data[0]['api_token']}&type=weekday"
        response = self.client.get(summary_url, content_type='application/json')
        self.assertEqual(response.data['data'][0]['day'], 'Tuesday')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_summary_language_time_api(self):
        """
        Test behaviour of GET request for getting summary by time taken in languages
        """
        summary_url = f"{self.summary_url}?api_token={timeLog_data[0]['api_token']}&type=language_total_time"
        response = self.client.get(summary_url, content_type='application/json')
        self.assertEqual(response.data['data'][0]['detected_language'], timeLog_data[0]['detected_language'])
        self.assertEqual(response.data['data'][0]['total_time'], timeLog_data[0]['end_timestamp']-timeLog_data[0]['start_timestamp'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_summary_file_names_api(self):
        """
        Test behaviour of GET request for getting summary by file names
        """
        summary_url = f"{self.summary_url}?api_token={timeLog_data[0]['api_token']}&type=file_name_total_time"
        response = self.client.get(summary_url, content_type='application/json')
        self.assertEqual(response.data['data'][0]['file_name'], timeLog_data[0]['file_name'])
        self.assertEqual(response.data['data'][0]['total_time'], timeLog_data[0]['end_timestamp']-timeLog_data[0]['start_timestamp'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_summary_user_stats_api(self):
        """
        Test behaviour of GET request for getting summary by overall user statistics
        """
        summary_url = f"{self.summary_url}?api_token={timeLog_data[0]['api_token']}&type=user_overall_stats"
        response = self.client.get(summary_url, content_type='application/json')
        self.assertEqual(response.data['data'][0]['total_languages'], 1)
        self.assertEqual(response.data['data'][0]['total_time'], timeLog_data[0]['end_timestamp']-timeLog_data[0]['start_timestamp'])
        self.assertEqual(response.data['data'][0]['total_files'], 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_summary_recent_stats_api(self):
        """
        Test behaviour of GET request for getting summary by recent user statistics
        """
        summary_url = f"{self.summary_url}?api_token={timeLog_data[0]['api_token']}&type=recent_stats"
        response = self.client.get(summary_url, content_type='application/json')
        self.assertEqual(response.data['data'][0]['file_count'], 1)
        self.assertEqual(response.data['data'][0]['language_count'], 1)
        self.assertEqual(response.data['data'][0]['total_time'], timeLog_data[0]['end_timestamp']-timeLog_data[0]['start_timestamp'])
        self.assertEqual(response.data['data'][0]['log_date'].isoformat(), timeLog_data[0]['log_date'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
