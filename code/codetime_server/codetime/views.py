from rest_framework import generics
from .request_handlers import handle_user_get, handle_user_post, handle_log_file_post, handle_summary_request, \
    handle_get_file_logs
from rest_framework.response import Response


class UserView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    """
    User View
    """

    def get(self, request, *args, **kwargs):
        """
        User get request
        """
        response = handle_user_get(request)
        return Response(data=response)

    def post(self, request, *args, **kwargs):
        """
        User post/signup and login request
        """
        response = handle_user_post(request)
        return Response(data=response, status=201)


class TimeLogView(generics.ListAPIView, generics.CreateAPIView):
    """
    TimeLog View
    """

    def post(self, request, *args, **kwargs):
        """
        TimeLog post request
        """
        response = handle_log_file_post(request)
        return Response(data=response, status=201)

    def get(self, request, *args, **kwargs):
        """
        TimeLog get request
        """
        response = handle_get_file_logs(request)
        return Response(data=response, status=response.get('status', 200))


class TimeLogSummaryView(generics.ListAPIView):
    """
    TimeLog Summary View
    """

    def get(self, request, *args, **kwargs):
        """
        TimeLogSummary get request
        """
        response = handle_summary_request(request)
        return Response(data=response)
