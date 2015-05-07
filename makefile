D=python manage.py

update_db:
	export DB_PORT_5432_TCP_ADDR=localhost && \
	$D makemigrations && \
	$D migrate

runserver:
	export DB_PORT_5432_TCP_ADDR=localhost && $(D) runserver

runserver_public:
	export DB_PORT_5432_TCP_ADDR=localhost && $D runserver 10.0.1.3:8000

collect_static:
	export DB_PORT_5432_TCP_ADDR=localhost && \
	$(D) collectstatic