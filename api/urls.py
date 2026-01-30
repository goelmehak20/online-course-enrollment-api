from django.urls import path
from .views import *

urlpatterns = [
    path('courses/', CourseListAPIView.as_view()),
    path('courses/<int:pk>/', CourseRetrieveUpdateDestroyAPIView.as_view()),

    path('enroll/', EnrollmentCreateAPIView.as_view()),
    path('enrollments/', EnrollmentListAPIView.as_view()),

    path('modules/', ModuleListCreateAPIView.as_view()),
    path('modules/<int:pk>/', ModuleRetrieveUpdateDestroyAPIView.as_view()),

]
