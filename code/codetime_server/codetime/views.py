from rest_framework import generics


class UserView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    
    def post(self, request, *args, **kwargs):
    
        pass