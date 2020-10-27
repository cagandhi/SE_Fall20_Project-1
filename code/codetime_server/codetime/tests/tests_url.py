# Create your tests here.
from django.test import SimpleTestCase
from django.urls import resolve, reverse
from ..views import TimeLogView, UserView, TimeLogSummaryView


# Create your tests here.


class TestURLs(SimpleTestCase):

    def test_time_log_resolution(self):
        url = reverse('timelog_url')
        self.assertEquals(resolve(url).func.view_class, TimeLogView)

    def test_user_url_resolution(self):
        url = reverse('user_endpoint')
        self.assertEquals(resolve(url).func.view_class, UserView)

    def test_summary_url_resolution(self):
        url = reverse('timelog_summary_url')
        self.assertEquals(resolve(url).func.view_class, TimeLogSummaryView)
