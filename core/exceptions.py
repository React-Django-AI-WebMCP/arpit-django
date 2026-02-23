"""
Custom exception handlers for consistent API error responses.
"""
import logging

from rest_framework.views import exception_handler

logger = logging.getLogger(__name__)


def custom_exception_handler(exc, context):  # noqa: ANN001, ANN201
    """Return consistent error format; log unexpected errors."""
    response = exception_handler(exc, context)
    if response is None:
        logger.exception("Unhandled exception", exc_info=exc)
    return response
