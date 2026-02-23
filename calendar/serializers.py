"""
DRF serializers for Calendar app. Fields per calendar-module-data-schema.md.
"""

from rest_framework import serializers

from .models import TimeEntry


class TimeEntrySerializer(serializers.ModelSerializer):
    """Serializer for time entry: task name, project, time (start/duration), entry_status, user."""

    user_id = serializers.PrimaryKeyRelatedField(source="user", read_only=True)  # Expose user id for filtering/display

    class Meta:
        model = TimeEntry
        fields = [
            "id",
            "task_name",
            "project",
            "start",
            "duration_minutes",
            "entry_status",
            "user_id",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at", "user_id"]


class TimeEntryCreateUpdateSerializer(serializers.ModelSerializer):
    """Create/update: Task Name, Project, Time (start, duration_minutes). User set from request."""

    class Meta:
        model = TimeEntry
        fields = ["task_name", "project", "start", "duration_minutes", "entry_status"]
