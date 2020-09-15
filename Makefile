
install:
	virtualenv -ppython3.7 .venv
	. .venv/bin/activate && pip install -r requirements.txt
	docker-compose up -d

start:
	docker-compose up -d
	. .venv/bin/activate && python -m phyto.database

stop:
	docker-compose down
