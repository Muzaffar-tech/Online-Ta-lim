from django.urls import path
from .views import CourseListCreateAPIView, LessonDetailAPIView

urlpatterns = [
    path('courses/', CourseListCreateAPIView.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseListCreateAPIView.as_view(), name='course-update'),
    path('lessons/<int:pk>/', LessonDetailAPIView.as_view(), name='lesson-detail'),
]
