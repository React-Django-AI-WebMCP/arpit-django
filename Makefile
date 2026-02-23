.PHONY: install run test lint migrate shell

install:
	pip install -r requirements/local.txt

run:
	python manage.py runserver

test:
	pytest

lint:
	black --check .
	isort --check-only .
	flake8 .

migrate:
	python manage.py migrate

shell:
	python manage.py shell
