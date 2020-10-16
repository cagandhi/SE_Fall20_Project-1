from rest_framework import generics
from .request_handlers import *
from rest_framework.response import Response


class UserView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    
    def post(self, request, *args, **kwargs):
        response = handle_user_post(request)
        return Response(data=response)
