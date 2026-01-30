import django_filters
from .models import Course
class CourseFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    created_by = django_filters.NumberFilter(field_name='created_by__id')
    created_at = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Course
        fields = ['title', 'created_by', 'created_at']
