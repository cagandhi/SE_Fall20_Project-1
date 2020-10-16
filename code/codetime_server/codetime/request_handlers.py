from .models import User
from .serializers import UserSerializer


def get_missing_param_response():
    return {
        "status": 1,
        "message": "Missing query parameter.",
        "data": []
    }


def get_serializer_error_response(error):
    
    error_response = {
        "status": 1,
        "data": [],
        "message": error
    }
    
    return error_response


def get_invalid_request_param(message):
    
    error_response = {
        "status": 1,
        "data": [],
        "message": message
    }
    
    return error_response


def handle_user_post(request):
    
    request_type = request.query_params.get("type", None)
    
    if request_type is None:
        return get_missing_param_response()
    
    if request_type == "login" or request_type == "signup":
        
        serializer = UserSerializer(request.data)
        
        if serializer.is_valid():
            return True
        else:
            return get_serializer_error_response(serializer.errors)
    
    else:
        
        return get_invalid_request_param("Invalid value for url param \"type\".")
