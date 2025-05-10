from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth.models import User

from .serializers import RegisterSerializer, ListUsersSerializer


class RegisterView(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = RegisterSerializer(data= data)

            if not serializer.is_valid():
                return Response({
                    'data': serializer.errors,
                    'message': 'something went wrong. Please try again.',
                    
                }, status= status.HTTP_400_BAD_REQUEST)
            
            serializer.save()
            return Response({
                'data': {},
                'message': 'User created successfully.',
            }, status= status.HTTP_201_CREATED)
        
        except Exception as e:
            print(e)
            return Response({
                'data': {},
                'message': 'something went wrong. Please try again.',

            }, status= status.HTTP_500_INTERNAL_SERVER_ERROR)


class ListUsersView(APIView):
    def get(self, request):
        try:
            users = User.objects.all()
            data = [
                {
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'username': user.username,
                } for user in users
            ]
            
            return Response({
                'data': data,
                'message': 'Users fetched successfully.',
            }, status= status.HTTP_200_OK)
           
        except Exception as e:
            print(e)
            return Response({
                'data': {},
                'message': 'something went wrong. Please try again.',
            }, status= status.HTTP_500_INTERNAL_SERVER_ERROR)
