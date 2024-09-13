from django.urls import path
from .views import *

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('feed/', FeedView.as_view(), name='feed'),
    path('login/', LoginView.as_view(), name='login'),
    path('follow/<int:profile_id>/', FollowView.as_view(), name='follow'),
    path('unfollow/<int:profile_id>/', UnfollowView.as_view(), name='unfollow'),
]
