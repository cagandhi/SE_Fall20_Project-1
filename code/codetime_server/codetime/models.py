from django.db import models
from django.utils.crypto import get_random_string
from django.utils.timezone import now
from django.core import serializers
import uuid
import json
from django.db.utils import IntegrityError

# Create your models here.


class UserManager(models.Manager):
    
    def get_user_from_username(self, username, password):
        
        user = self.filter(username=username, password=password).first()
        if user:
            return {
                "username": user.username,
                "password": user.password,
                "api_token": user.api_token
            }
        return None

    def get_user_from_api_token(self, api_token):
    
        user = self.filter(api_token=api_token).first()
        if user:
            return {
                "username": user.username,
                "password": user.password,
                "api_token": user.api_token
            }
        return None
    
    @staticmethod
    def create_user(user):
        
        user["api_token"] = str(uuid.uuid4())+get_random_string(length=16)

        user_instance = User(**user)
        try:
            if not user_instance.save():
                return 0
            return 1
        except IntegrityError as e:
            print(e)
            return 2
    
    def update_user(self, user, api_token):

        user_instance = self.filter(api_token=api_token)

        if user_instance:
            user_instance.update(**user)
            return 0
        return 1

    def login(self, username, password):

        user_info = self.filter(username=username, password=password).first()

        if user_info:
            return user_info["api_token"]
        return -1


class User(models.Model):

    class Meta:
        db_table = "log_user"

    log_user_id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, blank=False, null=False, max_length=100)
    password = models.CharField(blank=False, null=False, max_length=100)
    api_token = models.CharField(max_length=200)
    objects = UserManager()


class TimeLogManager(models.Manager):
    
    @staticmethod
    def create_log(time_log):
        
        time_log_instance = TimeLog(**time_log)
        
        try:
            
            if not time_log_instance.save():
                return 0
            return 1
        except:
            return 1

    def create_time_log(self, api_token, file_name, file_extension, 
                        detected_language, log_date, 
                        log_timestamp):

        try:
            user = User.objects.filter(api_token=api_token).first()
            file_log = self.filter(log_user_id=user, file_name=file_name).first()
            if file_log is not None:
                log_timestamp = file_log.log_timestamp + log_timestamp
                self.filter(log_user_id=user, file_name=file_name).update(log_timestamp=log_timestamp,
                        modified_at=now())
            else:
                self.create(log_user_id=user, file_name=file_name,
                                file_extension=file_extension, detected_language=detected_language,
                                log_date=log_date, log_timestamp=log_timestamp) 
            
            return api_token
        except Exception as e:
            print("error in creating logs for user " , e)
            return e

    def get_time_logs(self, api_token):

        try:
            logs = self.filter(api_token=api_token).all()
            return json.loads(serializers.serialize('json', [log for log in logs]))
        except Exception as e:
            print("error in getting logs for user ", e)
            return e


class TimeLog(models.Model):

    class Meta:
        db_table = "log_file_time"

    log_file_time_id = models.AutoField(primary_key=True)
    api_token = models.CharField(max_length=200, null=False, blank=False)
    file_name = models.CharField(max_length=1000, null=False, blank=False)
    file_extension = models.CharField(max_length=20, null=True, blank=True)
    detected_language = models.CharField(max_length=50, null=True, blank=True)
    log_date = models.DateField(blank=False, null=False)
    log_timestamp = models.FloatField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    objects = TimeLogManager()
