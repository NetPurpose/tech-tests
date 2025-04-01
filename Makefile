
install:
	virtualenv -ppython3.10 .venv
	. .venv/bin/activate && pip install -r requirements.txt
	docker-compose up -d

start:
	docker-compose up -d
	. .venv/bin/activate && python -m phyto.database

stop:
	docker-compose down

package:
	tar -cJvf tech_test.tar.xz --exclude=".git"  --exclude=".venv" --exclude="__pycache__" --exclude=".~lock*" \
		docker-compose.yaml \
		data \
		phyto \
		docker-compose.yaml \
		Makefile \
		README.md \
		requirements.txt
