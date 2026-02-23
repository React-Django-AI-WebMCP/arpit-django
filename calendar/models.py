"""
Calendar app models. Time entries per calendar-module-data-schema.md.
"""

from django.conf import settings
from django.db import models


class TimeEntry(models.Model):
    """
    A single time block on the calendar. Fields per data-schema only.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    task_name = models.CharField(max_length=255)
    project = models.CharField(max_length=255)
    start = models.DateTimeField(db_index=True)
    duration_minutes = models.PositiveIntegerField(help_text="Duration in minutes (for placement and resize).")
    entry_status = models.CharField(db_index=True, default="default", max_length=50)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="calendar_time_entries",
    )

    class Meta:
        ordering = ["start"]
        verbose_name = "time entry"
        verbose_name_plural = "time entries"
        indexes = [
            models.Index(fields=["user", "start"]),
            models.Index(fields=["project", "start"]),
        ]

    def __str__(self) -> str:
        return f"{self.task_name} @ {self.start}"
