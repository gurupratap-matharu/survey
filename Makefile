.PHONY: migrations
.PHONY: staticfiles
	
.PHONY: collectstatic run test ci 

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
	@docker compose exec web coverage run --source=. manage.py test -v 2

ci: test
	@docker compose exec web coverage report

isort:
	isort .

isort-check:
	isort -c .

makemigrations:
	docker compose exec web python manage.py makemigrations

migrate:
	docker compose exec web python manage.py migrate

check:
	docker compose exec web python manage.py check

check-deploy:
	docker compose exec web python manage.py check --deploy
