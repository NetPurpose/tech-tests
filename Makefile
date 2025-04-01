
setup-env:
	pyenv virtualenv 3.12 tech-test
	pyenv local tech-test

install:
	poetry install

start:
	docker compose up -d
	python -m phyto.database

stop:
	docker-compose down

run:
	python -m phyto.database
