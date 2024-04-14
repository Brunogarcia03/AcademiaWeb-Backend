from django.urls import path
from .views import (
    CategoryListAPIView,
    CourseListCreateAPIView,
    CourseRetrieveUpdateDestroyAPIView,
    VideoListCreateAPIView,
    VideoRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('courses/', CourseListCreateAPIView.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseRetrieveUpdateDestroyAPIView.as_view(), name='course-detail'),
    path('videos/', VideoListCreateAPIView.as_view(), name='video-list-create'),
    path('videos/<int:pk>/', VideoRetrieveUpdateDestroyAPIView.as_view(), name='video-detail'),
]
