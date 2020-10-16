from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    
    username = serializers.CharField(max_length=100, required=True)
    password = serializers.CharField(max_length=100, required=True)
    
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
