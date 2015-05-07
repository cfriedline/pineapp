D=python manage.py

update_db:
	$D makemigrations
	$D migrate

runserver:
	$D runserver

runserver_public:
	$D runserver 10.0.1.3:8000
