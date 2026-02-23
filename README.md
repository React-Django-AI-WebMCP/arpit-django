# Django Backend

Django REST API backend (Time Tracker – Nexus). Calendar module and health checks.

## Features

- Django 5.x with REST Framework
- Split settings: `config.settings.base`, `local`, `production`
- Core app: health (`/health/`), readiness (`/ready/`), logging, middleware
- Calendar app: placeholder for Calendar Module (time entries)
- CORS, JWT-ready (djangorestframework-simplejwt), python-decouple for env

## Quick start

```bash
# Create venv and install
python -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\activate on Windows
pip install -r requirements/local.txt

# Copy env and run
cp .env.example .env
python manage.py migrate
python manage.py runserver
```

- **Health:** http://localhost:8000/health/
- **Ready:** http://localhost:8000/ready/
- **Calendar API:** http://localhost:8000/api/calendar/
- **Admin:** http://localhost:8000/admin/

## Environment variables

See `.env.example`. Key ones: `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, `DB_*`, `CORS_ALLOWED_ORIGINS`.

## Docker

```bash
docker compose up --build
```

Runs web on port 8000, PostgreSQL and Redis as dependencies.

## Development

- **Lint:** `make lint` or `black . && isort . && flake8 .`
- **Tests:** `make test` or `pytest`
- **Migrations:** `make migrate` or `python manage.py migrate`

## Project structure

- `config/` – Django project (settings, urls, wsgi/asgi)
- `core/` – Shared app (health, logging, middleware, base models)
- `calendar/` – Calendar module app (models, serializers, services, views)
- `requirements/` – base.txt, local.txt, production.txt
- `logs/` – Application logs (create with `.gitkeep`)

## Documentation

- [Calendar module requirement & UI](docs/calendar-module-requirement-and-ui.md)
- [Calendar module epic](docs/calendar-module-epic.md)
