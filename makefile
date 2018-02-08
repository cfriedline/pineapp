D=python manage.py

update_db:
	export DB_PORT_5432_TCP_ADDR=localhost && \
	$D makemigrations && \
	$D migrate

runserver:
	export DB_PORT_5432_TCP_ADDR=localhost && $(D) runserver

runserver_public:
	export DB_PORT_5432_TCP_ADDR=localhost && $D runserver 0.0.0.0:8000

collect_static:
	export DB_PORT_5432_TCP_ADDR=localhost && \
	$(D) collectstatic

backup_db:
	pg_dump pineapp > pineapp.bak
