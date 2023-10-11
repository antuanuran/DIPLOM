TIME_MARK:=$(shell date +%FT%H-%M)

docer_run:
	docker-compose up -d


dumpdb: docer_run
	sleep 5
	python manage.py migrate
	mkdir -p _dumps
	python manage.py dumpdata --indent 2 \
		--exclude auth.permission \
		--exclude contenttypes \
		--exclude admin.logentry \
		--exclude sessions.session \
		> _dumps/db-${TIME_MARK}.json

recreatedb: dumpdb
	docker-compose down -v
	docker-compose up -d
	sleep 5
	python manage.py migrate
	python manage.py createsuperuser

run_project: recreatedb
	python manage.py loaddata _dumps/db-${TIME_MARK}.json
	python manage.py import_data data_all/import_2.yaml --owner_id 1
	python manage.py import_data data_all/import_1.csv --owner_id 1
	python manage.py import_data data_all/import_3.yml --owner_id 1
	python manage.py runserver

