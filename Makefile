#backend
install_backend:
	virtualenv backend/env; \
	source backend/env/bin/activate; \
	pip install -r backend/requirements.txt

reset_database:
	rm backend/api/migrations/0001_initial.py; \
	rm backend/db.sqlite3; \
	source backend/env/bin/activate; \
	python backend/manage.py migrate; \
	python backend/manage.py makemigrations; \
	python backend/manage.py migrate; \
	python backend/init_db.py
	
run_backend:
	source backend/env/bin/activate; \
	python backend/manage.py runserver

deploy_backend:
	make install_backend; \
	make reset_database; \
	make run_backend

run_reset_db_backend:
	make reset_database; \
	make run


run_test_backend:
	source backend/env/bin/activate; \
	make reset_database; \
	cd backend; \
	pytest

#frontend
install_frontend:
	cd frontend; \
	npm install

run_frontend:
	cd frontend; \
	npm run serve

deploy_frontend:
	make install_frontend; \
	make run_frontend