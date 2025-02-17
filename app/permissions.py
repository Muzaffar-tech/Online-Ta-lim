from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return request.user and request.user.is_staff

class IsEnrolled(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.enrollments.filter(user=request.user).exists() or request.user.is_staff
