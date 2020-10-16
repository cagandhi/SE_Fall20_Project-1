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


def get_valid_output_response(data):
    
    response = {
        "status": 0,
        "message": "Success",
        "data": data
    }

    return response


def get_something_went_wrong_response(data=None):
    
    response = {
        "status": 1,
        "message": "Something went wrong",
        "data": data
    }
    
    return response


def get_invalid_user_credentials(data=None):
    
    response = {
        "status": 1,
        "message": "Invalid user credentials.",
        "data": data
    }
    
    return response


def handle_user_post(request):
    
    request_type = request.query_params.get("type", None)
    
    if request_type is None:
        return get_missing_param_response()
    
    if request_type == "login" or request_type == "signup":
        
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            if request_type == "signup":
                return_status = User.objects.create_user(request.data)
                
                if return_status == 0:
                    data = User.objects.get_user_from_username(request.data["username"])
                    return get_valid_output_response(data)
                elif return_status == 1:
                    return get_something_went_wrong_response(request.data)
                elif return_status == 2:
                    return {
                        "status": 1,
                        "message": "Username already taken.",
                        "data": request.data
                    }
            elif request_type == "login":
                
                return_status = User.objects.get_user_from_username(request.data["username"],
                                                                    request.data["password"])
                
                if return_status:
                    return get_valid_output_response(return_status)
                else:
                    return get_invalid_user_credentials(request.data)
        else:
            return get_serializer_error_response(serializer.errors)
    
    else:
        return get_invalid_request_param("Invalid value for url param \"type\".")
