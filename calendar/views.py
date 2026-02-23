"""
Calendar API views. List entries (date range), CRUD single entry. Per tech-doc-02, tech-doc-03.
Auth skipped for now: unauthenticated requests use a default user and can CRUD any entry.
"""

from datetime import datetime
from typing import Any

from django.contrib.auth import get_user_model
from django.utils.dateparse import parse_datetime
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.responses import APIResponse

from .models import TimeEntry
from .serializers import TimeEntryCreateUpdateSerializer, TimeEntrySerializer

User = get_user_model()


def _effective_user(request: Request):
    """User for this request. Authenticated => request.user; else default dev user (auth skipped for now)."""
    if request.user and request.user.is_authenticated:
        return request.user
    user, created = User.objects.get_or_create(
        username="default_calendar_user",
        defaults={"email": "dev@local.local", "is_staff": False, "is_superuser": False},
    )
    if created:
        user.set_unusable_password()
        user.save()
    return user


class TimeEntryViewSet(ModelViewSet):
    """
    List: GET /api/calendar/entries/?start=...&end=... (ISO date/datetime).
    Create: POST /api/calendar/entries/
    Retrieve: GET /api/calendar/entries/{id}/
    Update: PATCH /api/calendar/entries/{id}/
    Delete: DELETE /api/calendar/entries/{id}/
    """

    queryset = TimeEntry.objects.all().select_related("user")
    serializer_class = TimeEntrySerializer
    pagination_class = None  # Set in list() after we wrap response

    def _parse_start_end(self, request: Request) -> tuple[datetime | None, datetime | None]:
        """Parse start and end query params (ISO date or datetime)."""
        start_s = request.query_params.get("start")
        end_s = request.query_params.get("end")
        start_dt = parse_datetime(start_s) if start_s else None
        end_dt = parse_datetime(end_s) if end_s else None
        return start_dt, end_dt

    def get_queryset(self):
        qs = super().get_queryset()
        # Auth skipped for now: when authenticated filter by user; when not, show all
        if self.request.user and self.request.user.is_authenticated:
            qs = qs.filter(user=self.request.user)
        return qs

    def list(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """GET /api/calendar/entries/?start=...&end=... Pagination per project standards."""
        start_dt, end_dt = self._parse_start_end(request)
        qs = self.get_queryset()
        if start_dt is not None:
            qs = qs.filter(start__gte=start_dt)
        if end_dt is not None:
            # Entries that start before end (or that overlap: end of entry = start + duration)
            qs = qs.filter(start__lt=end_dt)
        page_size = int(request.query_params.get("page_size", 100))
        page = int(request.query_params.get("page", 1))
        offset = (page - 1) * page_size
        page_slice = list(qs[offset : offset + page_size + 1])
        items = page_slice[:page_size]
        has_next = len(page_slice) > page_size
        data = {
            "items": TimeEntrySerializer(items, many=True).data,
            "page": page,
            "page_size": page_size,
            "has_next": has_next,
        }
        return Response(
            APIResponse.success(data=data, message="OK", status_code=200),
            status=status.HTTP_200_OK,
        )

    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """POST with task_name, project, start, duration_minutes, entry_status. User from request (or default)."""
        ser = TimeEntryCreateUpdateSerializer(data=request.data)
        if not ser.is_valid():
            return Response(
                APIResponse.error(
                    message="Validation failed",
                    errors=ser.errors,
                    error_code="VALIDATION_ERROR",
                    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                ),
                status=status.HTTP_422_UNPROCESSABLE_ENTITY,
            )
        entry = ser.save(user=_effective_user(request))
        return Response(
            APIResponse.success(
                data=TimeEntrySerializer(entry).data,
                message="Created",
                status_code=status.HTTP_201_CREATED,
            ),
            status=status.HTTP_201_CREATED,
        )

    def retrieve(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """GET /api/calendar/entries/{id}/"""
        entry = self.get_object()
        return Response(
            APIResponse.success(data=TimeEntrySerializer(entry).data),
            status=status.HTTP_200_OK,
        )

    def partial_update(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """PATCH /api/calendar/entries/{id}/ (auth skipped for now: any user can update)."""
        entry = self.get_object()
        ser = TimeEntryCreateUpdateSerializer(entry, data=request.data, partial=True)
        if not ser.is_valid():
            return Response(
                APIResponse.error(
                    message="Validation failed",
                    errors=ser.errors,
                    error_code="VALIDATION_ERROR",
                    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                ),
                status=status.HTTP_422_UNPROCESSABLE_ENTITY,
            )
        ser.save()
        entry.refresh_from_db()
        return Response(
            APIResponse.success(data=TimeEntrySerializer(entry).data),
            status=status.HTTP_200_OK,
        )

    def destroy(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """DELETE /api/calendar/entries/{id}/ -> 204 No Content (auth skipped for now)."""
        entry = self.get_object()
        entry.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
