"""
Unified API response helpers. All endpoints use this shape per api-response-rules.
"""


class APIResponse:
    """Consistent JSON shape for success and error responses."""

    @staticmethod
    def success(data=None, message: str = "OK", status_code: int = 200) -> dict:
        """Build success payload. Use with Response(..., status=status_code)."""
        return {"status": status_code, "message": message, "data": data}

    @staticmethod
    def error(
        message: str = "Error",
        *,
        errors: dict | None = None,
        error_code: str | None = None,
        status_code: int = 400,
    ) -> dict:
        """Build error payload. Use with Response(..., status=status_code)."""
        body: dict = {"status": status_code, "message": message}
        if errors is not None:
            body["errors"] = errors
        if error_code is not None:
            body["error_code"] = error_code
        return body
