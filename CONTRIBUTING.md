# Contributing

## Git workflow

- **main** – production-ready
- **develop** – integration
- **feature/<name>** – from develop
- **bugfix/<name>** – from develop
- **hotfix/<name>** – from main

## Commit messages

Format: `type(scope): subject`

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `perf`, `ci`, `build`

Examples:

- `feat(calendar): add event creation endpoint`
- `fix(core): resolve health check response shape`
- `docs(readme): update quick start`

## Development setup

1. Clone and create venv; install from `requirements/local.txt`.
2. Copy `.env.example` to `.env` and set `SECRET_KEY` and any DB/CORS values.
3. Run `python manage.py migrate`.
4. Run tests: `pytest`. Run lint: `make lint` (Black, isort, flake8).

## Code review checklist

- [ ] Code follows project style (Black, isort, flake8)
- [ ] Tests added/updated and passing
- [ ] No new security or performance issues
- [ ] Docstrings/type hints where appropriate
