from rest_framework import generics, permissions
from .models import Course, Enrollment, Module
from .serializers import CourseSerializer, EnrollmentSerializer, ModuleSerializer


class CourseListAPIView(generics.ListAPIView):
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Course.objects.prefetch_related('modules')
        title = self.request.query_params.get('title')
        created_by = self.request.query_params.get('created_by')
        if title:
            queryset = queryset.filter(title__icontains=title)
        if created_by:
            queryset = queryset.filter(created_by=created_by)
        return queryset

class CourseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.select_related('created_by')
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]


class EnrollmentCreateAPIView(generics.CreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [permissions.IsAuthenticated]


class EnrollmentListAPIView(generics.ListAPIView):
    serializer_class = EnrollmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = Enrollment.objects.filter(student=self.request.user).select_related('student').prefetch_related('courses')
        status = self.request.query_params.get('status')
        if status:
            qs = qs.filter(status=status)
        return qs


class EnrollmentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enrollment.objects.select_related('student').prefetch_related('courses')
    serializer_class = EnrollmentSerializer
    permission_classes = [permissions.IsAuthenticated]


class ModuleListCreateAPIView(generics.ListCreateAPIView):
    queryset = Module.objects.select_related('course')
    serializer_class = ModuleSerializer
    permission_classes = [permissions.IsAuthenticated]


class ModuleRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Module.objects.select_related('course')
    serializer_class = ModuleSerializer
    permission_classes = [permissions.IsAuthenticated]
