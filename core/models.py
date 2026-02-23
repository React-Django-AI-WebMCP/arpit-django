"""
Abstract base models (e.g. TimeStampedModel, SoftDeleteModel).
"""
from django.db import models


class TimeStampedModel(models.Model):
    """Abstract model with created_at and updated_at."""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SoftDeleteModel(models.Model):
    """Abstract model with soft delete via is_deleted."""

    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True
