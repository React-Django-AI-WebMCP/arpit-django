"""
Calendar app URL routing. /api/calendar/ is prefixed in config/urls.py.
"""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import TimeEntryViewSet

router = DefaultRouter()
router.register("entries", TimeEntryViewSet, basename="calendar-entries")

urlpatterns = [
    path("", include(router.urls)),
]
