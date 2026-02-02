from django.urls import path
from django.shortcuts import redirect
from . import views

def api_root(request):
    return redirect("/api/schema/swagger-ui/")

urlpatterns = [
    # 👇 API FALLBACK
    path("", api_root),

    # Your APIs
    path("courses/", views.CourseListAPIView.as_view()),
    path("enrollments/", views.EnrollmentListAPIView.as_view()),
    path("enroll/", views.EnrollmentCreateAPIView.as_view()),
    path("modules/", views.ModuleListCreateAPIView.as_view()),

    # Docs
    path("schema/", views.schema_view, name="schema"),
    path("schema/swagger-ui/", views.swagger_ui, name="swagger-ui"),
    path("schema/redoc/", views.redoc, name="redoc"),
]
