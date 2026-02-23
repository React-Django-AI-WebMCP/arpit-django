"""
Base permission classes for API views.
"""
from rest_framework import permissions


class IsAuthenticatedReadOnly(permissions.BasePermission):
    """Allow read-only for authenticated users."""

    def has_permission(self, request, view):  # noqa: ANN001
        if request.method in permissions.SAFE_METHODS:
            return request.user and request.user.is_authenticated
        return False
