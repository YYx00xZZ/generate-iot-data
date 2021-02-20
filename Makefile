SHELL := /bin/bash

clear:
	rm -rf output/ gen_clients/

gen_some:
	python runner.py generate 4 --token=$(FLESPI_TOKEN)

start_all:
	python conc.py

# install:
# 	pipenv install

# activate:
# 	pipenv shell

# run:
# 	python manage.py runserver

# migration:
# 	python manage.py makemigrations

# migrate:
# 	python manage.py migrate

# superuser:
# 	python manage.py createsuperuser

# heroku:
# 	git push heroku master

# deploy:
# 	docker-compose build
# 	docker-compose up -d

# down:
# 	docker-compose down
