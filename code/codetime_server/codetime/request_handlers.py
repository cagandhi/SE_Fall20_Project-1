from .models import User, TimeLog
from .serializers import UserSerializer, TimeLogSerializer


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


def handle_log_file_post(request):

    print(request.data)
    serializer = TimeLogSerializer(data=request.data)
    if serializer.is_valid():
        data = serializer.data
        status = TimeLog.objects.create_time_log(data["api_token"],
                                                 data["file_name"], data["file_extension"], 
                                                 data["detected_language"], data["log_date"], 
                                                 data["log_timestamp"])
        return status
    else:
        return get_serializer_error_response(serializer.errors)
