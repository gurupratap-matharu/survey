APP_LIST ?= core users pages surveys

.PHONY: collectstatic run test ci migrations staticfiles 

help:
	@echo "Available commands"
	@echo " - run		: builds docker images and shows logs"
	@echo " - ci		: lints, checks migrations, runs tests and shows coverage report"
	@echo " - shell		: launches the django shell"
	@echo " - isort		: sorts all imports of the project"
	@echo " - lint		: lints the code"

collectstatic:
	docker compose exec web python manage.py collectstatic --noinput

clean:
	docker compose exec web rm -rf __pycache__ .pytest_cache
	rm -rf __pycache__ .pytest_cache

up:
	docker compose up -docker

down:
	docker compose down
	
build:
	docker compose down
	docker compose up -d --build

logs:
	docker compose logs -f web

run:
	docker compose down
	docker compose up -d --build
	docker compose logs -f

shellplus:
	docker compose exec web python manage.py shell_plus

shell:
	docker compose exec web python manage.py shell

showmigrations:
	docker compose exec web python manage.py showmigrations

migrations-check:
	docker compose exec web python manage.py makemigrations --check --dry-run

test: migrations-check
	docker compose exec web coverage run --source=. manage.py test -v 2

ci: lint test
	docker compose exec web coverage report

isort:
	isort .

isort-check:
	isort -c .

lint: isort
	docker compose exec web pylint $(APP_LIST)
	
makemigrations:
	docker compose exec web python manage.py makemigrations

migrate:
	docker compose exec web python manage.py migrate

check:
	docker compose exec web python manage.py check

check-deploy:
	docker compose exec web python manage.py check --deploy
