
from django.conf.urls import url
from .views import UserView


urlpatterns = [
    url('user/', UserView.as_view(), name='user_endpoint'),
]
