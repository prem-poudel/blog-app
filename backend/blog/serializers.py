from rest_framework import serializers

from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        exclude = ['created_at', 'updated_at']

class PublicBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'