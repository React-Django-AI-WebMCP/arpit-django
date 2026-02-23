"""
Health check views: /health/ and /ready/.
"""
from django.db import connection
from django.http import JsonResponse
from django.views import View


class HealthCheckView(View):
    """Basic liveness: returns 200 OK."""

    def get(self, request):  # noqa: ANN001
        return JsonResponse({"status": "ok"})


class ReadinessCheckView(View):
    """Readiness: checks DB (and optionally cache) connectivity."""

    def get(self, request):  # noqa: ANN001
        try:
            connection.ensure_connection()
        except Exception:  # noqa: BLE001
            return JsonResponse({"status": "unhealthy", "database": "disconnected"}, status=503)
        return JsonResponse({"status": "ok", "database": "connected"})
