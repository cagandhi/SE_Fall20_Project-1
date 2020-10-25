from django.test import TestCase

# Create your tests here.
from django.test import SimpleTestCase
from django.urls import resolve, reverse
import codeTime.views
# Create your tests here.


class TestURLs(SimpleTestCase):

    def test_time_log_resolution(self):
        url = reverse('timelog')
        self.assertEquals(resolve(url).func.view_class, codeTime.views.TimeLogView)

    def test_user_url_resolution(self):
        url = reverse('user')
        self.assertEquals(resolve(url).func.view_class, codeTime.views.UserView)