# Created by Ayushi Rajendra Kumar at 10/25/2020

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
# Enter steps here

import copy
from django.test import TestCase, Client
from django.urls import reverse
from django.core import serializers
import codetime.views
from codetime.models import TimeLog, User

users_date = {
    "log_user_id": 123,
    "username": "ayushi",
    "password": "123ayushi",
    "api_token": "1234abcd",

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
