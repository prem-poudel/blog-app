from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterSerializer(serializers.Serializer):
    
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        if User.objects.filter(username= data['username']).exists():
            raise serializers.ValidationError("Usernama already taken.")
        

        return data
    
    def create(self, validated_data):
        user = User.objects.create(
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            username = validated_data['username'].lower(),
        )

        user.set_password(validated_data['password'])
        user.save()

        return validated_data
    
class ListUsersSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()


class LoginSerializer(serializers.Serializer):
    username= serializers.CharField()
    password= serializers.CharField()

    def validate(self, data):
        print(data)
        if not  User.objects.filter(username= data['username']).exists():
            raise serializers.ValidationError("Account not found.")
        
        return data
        
    # if user is valid, get jwt token
    def get_jwt_token(self, data):
        user = authenticate(
            username= data['username'],
            password= data['password']
        )

        if not user:
            return {
                'data': {},
                'message': 'Invalid credentials.',
            }
        
        refresh = RefreshToken.for_user(user)

        return {
            'data': {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            },
            'message': 'Login successful.',
            
        }
