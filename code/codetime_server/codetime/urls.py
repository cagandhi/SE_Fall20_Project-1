from django.conf.urls import url
from codetime.views import UserView, TimeLogView


urlpatterns = [url('user', UserView.as_view(), name='user_url'),
               url('timelog', TimeLogView.as_view(), name='timelog_url')]
