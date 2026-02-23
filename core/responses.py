"""
Unified API response structure (success and error).
"""
from rest_framework.response import Response


def success_response(data=None, message: str = "OK", status: int = 200) -> Response:
    """Return a consistent success payload."""
    payload = {"success": True, "message": message, "data": data}
    return Response(payload, status=status)


def error_response(
    message: str,
    *,
    errors: dict | None = None,
    error_code: str | None = None,
    status: int = 400,
) -> Response:
    """Return a consistent error payload."""
    payload = {"success": False, "message": message}
    if errors is not None:
        payload["errors"] = errors
    if error_code is not None:
        payload["error_code"] = error_code
    return Response(payload, status=status)
