"""
Production settings. Debug=False, security hardening.
"""

from .base import *  # noqa: F401, F403

DEBUG = False
ALLOWED_HOSTS = []  # Set via env in production

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"
