"""
API views / ViewSets for Calendar app.
"""
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


@api_view(["GET"])
@permission_classes([AllowAny])
def calendar_root(request):  # noqa: ANN001
    """Placeholder root for calendar API."""
    return Response({"message": "Calendar API"}, status=200)
