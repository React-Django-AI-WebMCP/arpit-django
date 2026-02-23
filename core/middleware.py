"""
Custom middleware (e.g. request logging with timing).
"""
import logging
import time

logger = logging.getLogger(__name__)


class RequestLoggingMiddleware:
    """Log each request with method, path, status, and duration."""

    def __init__(self, get_response):  # noqa: ANN001
        self.get_response = get_response

    def __call__(self, request):  # noqa: ANN001
        start = time.monotonic()
        response = self.get_response(request)
        duration_ms = (time.monotonic() - start) * 1000
        logger.info(
            "%s %s %s %.2fms",
            request.method,
            request.path,
            response.status_code,
            duration_ms,
        )
        return response
