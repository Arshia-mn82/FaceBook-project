from .views import *
from django.urls import path

urlpatterns = [
    path("allposts/", PostList.as_view()),
    path("allposts/<int:pk>", PostDetail.as_view()),
    path("deletepost/<int:pk>", PostDetail.as_view()),
    path("updatepost/<int:pk>", PostDetail.as_view()),
    path("createpost/", PostList.as_view()),
    path('like/', add_like),
]
