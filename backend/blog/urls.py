from django.urls import path
from .views import BlogView

urlpatterns = [
  path("add-blog/", BlogView.as_view(), name="add_blog"),
]