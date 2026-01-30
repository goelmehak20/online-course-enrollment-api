from rest_framework import permissions
class IsInstructor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'Instructor'

class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'Student'

