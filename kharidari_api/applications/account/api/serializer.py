from ..models import User
from rest_framework import serializers
import re


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'gender', 'date_of_birth']
        
    def validate_password(self, value):
        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$" 
        pattern = re.compile(reg)
        match = re.search(pattern, value)
        if match:
            return value
        else:
            raise serializers.ValidationError("Password must be atleast 6 charcter long and must have one upper, one lower, one number and one special character")


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()