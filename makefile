D=python manage.py

update_db:
	$D makemigrations
	$D migrate

runserver:
	$D runserver
