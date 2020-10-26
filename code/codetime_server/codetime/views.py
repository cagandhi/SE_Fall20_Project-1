from rest_framework import generics
from .request_handlers import *
from rest_framework.response import Response


class UserView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    
    def get(self, request, *args, **kwargs):
        response = handle_user_get(request)
        return Response(data=response)
    
    def post(self, request, *args, **kwargs):
        response = handle_user_post(request)
        return Response(data=response)


class TimeLogView(generics.ListAPIView, generics.CreateAPIView):
    
    def post(self, request, *args, **kwargs):
        response = handle_log_file_post(request)
        return Response(data=response, status=200)

    def get(self, request, *args, **kwargs):
        response = handle_get_file_logs(request)
        return Response(data=response, status=response.get('status', 200))


class TimeLogSummaryView(generics.ListAPIView):
    
    def get(self, request, *args, **kwargs):
        response = handle_summary_request(request)
        return Response(data=response)
