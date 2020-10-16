from rest_framework import generics
from .request_handlers import *
from rest_framework.response import Response


class UserView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    
    def post(self, request, *args, **kwargs):
        response = handle_user_post(request)
        return Response(data=response)

class TimeLogView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    
    def post(self, request, *args, **kwargs):
        status = handle_log_file_post(request)
        if status == 0:
            return Response(data="Error Occured", status=400)
        else:
            return Response(data="Successful Request", status=200)

    def get(self, request, *args, **kwargs):
        pass
