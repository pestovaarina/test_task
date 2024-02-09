from django.urls import path

from .views import APIPost, APIPostDetail


urlpatterns = [
    path('posts/', APIPost.as_view()),
    path('posts/<int:pk>/', APIPostDetail.as_view())
]
