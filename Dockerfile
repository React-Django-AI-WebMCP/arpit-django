# Multi-stage build for production
FROM python:3.12-slim as builder
WORKDIR /app
RUN pip install --no-cache-dir --upgrade pip
COPY requirements/production.txt .
RUN pip install --no-cache-dir -r production.txt

FROM python:3.12-slim as runtime
ENV PYTHONUNBUFFERED=1
RUN useradd --create-home appuser
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY . .
RUN chown -R appuser:appuser /app
USER appuser
EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health/')" || exit 1
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]
