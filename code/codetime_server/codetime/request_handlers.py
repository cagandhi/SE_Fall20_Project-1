from .models import User, TimeLog
from .serializers import UserSerializer, TimeLogSerializer


def get_missing_param_response(data=None):

    return {
        "status": 400,
        "message": "Missing query parameter.",
        "data": data
    }


def get_serializer_error_response(error):

    error_response = {
        "status": 422,
        "data": [],
        "message": error
    }
    return error_response


def get_invalid_request_param(message):

    error_response = {
        "status": 400,
        "data": [],
        "message": message
    }
    return error_response


def get_valid_output_response(data):
    
    response = {
        "status": 200,
        "message": "Success",
        "data": data
    }

    return response


def get_something_went_wrong_response(data=None):
    
    response = {
        "status": 500,
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
                    data = User.objects.get_user_from_username(request.data["username"], request.data["password"])
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


def handle_log_file_post(request):

    serializer = TimeLogSerializer(data=request.data)
    if serializer.is_valid():
        data = serializer.data
        response = TimeLog.objects.create_time_log(data["api_token"],
                                                 data["file_name"], data["file_extension"], 
                                                 data["detected_language"], data["log_date"], 
                                                 data["log_timestamp"])
        if response==data["api_token"]:
            return get_valid_output_response(response)
        else:
            return get_something_went_wrong_response(response)
    else:
        return get_serializer_error_response(serializer.errors)

def handle_get_file_logs(request):

    user_api_token = request.query_params.get("api_token", None)
    if user_api_token is not None:
        response = TimeLog.objects.get_time_logs(user_api_token)
        if isinstance(response, list):
            return get_valid_output_response(response)
        else:
            return get_invalid_request_param(response)
    else:
        return get_missing_param_response("api_token")
