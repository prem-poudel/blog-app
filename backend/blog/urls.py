from django.urls import path
from .views import BlogView, PublicBlogView

urlpatterns = [
  path("user/", BlogView.as_view(), name="user_blogs"),
  path("public/", PublicBlogView.as_view(),name="public_blogs"),
]