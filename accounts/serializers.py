from .models import CustomUser
from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= CustomUser
        fields= ('username', 'first_name', 'last_name', 'email', 'phone', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

