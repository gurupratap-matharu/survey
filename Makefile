.PHONY: migrations
.PHONY: staticfiles

test:
	docker compose exec web python manage.py test -v 2

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

buildlogs:
	docker compose down
	docker compose up -d --build
	docker compose logs -f

shellplus:
	docker compose exec web python manage.py shell_plus

shell:
	docker compose exec web python manage.py shell

showmigrations:
	docker compose exec web python manage.py showmigrations

makemigrations:
	docker compose exec web python manage.py makemigrations

migrate:
	docker compose exec web python manage.py migrate

check:
	docker compose exec web python manage.py check

check-deploy:
	docker compose exec web python manage.py check --deploy
