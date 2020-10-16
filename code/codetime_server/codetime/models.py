from django.db import models
from django.utils.crypto import get_random_string
import uuid

# Create your models here.


class UserManager(models.Manager):
    
    @staticmethod
    def create_user(user):
        
        user_instance = User(**user)
        
        if not user_instance.save():
            return 0
        return 1
    
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
    username = models.CharField(blank=False, null=False, max_length=100)
    password = models.CharField(blank=False, null=False, max_length=100)
    api_token = models.CharField(default=str(uuid.uuid4())+get_random_string(length=16))
    objects = UserManager()


class TimeLogManager(models.Manager):
    pass


class TimeLog(models.Model):
    
    class Meta:
        db_table = "log_file_time"
    
    log_file_time_id = models.AutoField(primary_key=True)
    log_user_id = models.ForeignKey(to=User, related_name="user_id", on_delete=models.CASCADE)
    file_name = models.CharField(max_length=1000, null=False, blank=False)
    file_extension = models.CharField(max_length=20, null=True, blank=True)
    detected_language = models.CharField(max_length=50, null=True, blank=True)
    log_date = models.DateField(blank=False, null=False)
    log_timestamp = models.FloatField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    objects = TimeLogManager()
