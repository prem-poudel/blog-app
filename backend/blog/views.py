from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import BlogSerializer
from .models import Blog


# Public Blog View

class PublicBlogView(APIView):
    def get(self, request):
        try:
            blogs = Blog.objects.all()
            serializer = BlogSerializer(blogs, many=True)
            if not serializer.data:
                return Response({
                    'data': serializer.data,
                    'message': 'No blogs found',
                }, status=status.HTTP_404_NOT_FOUND)
            return Response({
                'data': serializer.data,
                'message': 'Blogs fetched successfully',
            }, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                'data': str(e),
                'message': 'Something went wrong',
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class BlogView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        try:
            blogs= Blog.objects.filter(user =request.user)
            serializer = BlogSerializer(blogs, many=True)
            return Response({
                'data': serializer.data,
                'message': 'Blogs fetched successfully',
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'data': str(e),
                'message': 'Something went wrong',
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



    def post(self, request):
        try:
            data = request.data
            data['user'] = request.user.id
            serializer = BlogSerializer(data=data)

            if not serializer.is_valid():
                return Response({
                    'data': serializer.errors,
                    'message': 'Something went wrong',
                }, status=status.HTTP_400_BAD_REQUEST)
            
            serializer.save(user=request.user)
            
            return Response({
                'data': serializer.data,
                'message': 'Blog created successfully',
            }, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({
                'data': str(e),
                'message': 'Something went wrong',
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    