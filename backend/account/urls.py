from django.urls import path
from .views import RegisterView, ListUsersView
urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),     # reister view
    path("users/", ListUsersView.as_view(), name="list_users"),  # list users view
    
]