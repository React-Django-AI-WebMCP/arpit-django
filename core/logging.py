"""
Logging configuration. JSON formatter for production, console for dev.
"""
import json
import logging
from pathlib import Path

from django.conf import settings


class JSONFormatter(logging.Formatter):
    """Format log records as JSON for production."""

    def format(self, record: logging.LogRecord) -> str:
        log_data = {
            "timestamp": self.formatTime(record),
            "level": record.levelname,
            "message": record.getMessage(),
            "logger": record.name,
        }
        if record.exc_info:
            log_data["exception"] = self.formatException(record.exc_info)
        return json.dumps(log_data)


def configure_logging() -> None:
    """Configure log handlers and levels."""
    log_level = "DEBUG" if getattr(settings, "DEBUG", False) else "INFO"
    logs_dir = Path(settings.BASE_DIR) / "logs"
    logs_dir.mkdir(exist_ok=True)

    handlers: list[logging.Handler] = [
        logging.StreamHandler(),
    ]
    if not settings.DEBUG:
        file_handler = logging.FileHandler(logs_dir / "app.log", encoding="utf-8")
        file_handler.setFormatter(JSONFormatter())
        handlers.append(file_handler)

    logging.basicConfig(
        level=log_level,
        format="%(asctime)s %(levelname)s [%(name)s] %(message)s",
        handlers=handlers,
    )
