TIME_MARK:=$(shell date +%FT%H-%M)

dumpdb:
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

load_db: recreatedb
	python manage.py loaddata _dumps/db-${TIME_MARK}.json
	python manage.py runserver



