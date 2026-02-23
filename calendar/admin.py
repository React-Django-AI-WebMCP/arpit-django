from django.contrib import admin

from .models import TimeEntry


@admin.register(TimeEntry)
class TimeEntryAdmin(admin.ModelAdmin):
    list_display = ("id", "task_name", "project", "start", "duration_minutes", "entry_status", "user")
    list_filter = ("entry_status", "project")
    search_fields = ("task_name", "project")
