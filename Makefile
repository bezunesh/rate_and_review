all: setup  migrate collect_static

setup:
	python3 -m venv .venv
	. .venv/bin/activate && \
	pip install --upgrade pip && \
    pip install -r requirements.txt

migrate:
	# Run database migrations
	. .venv/bin/activate && \
	python3 manage.py migrate

run_dev:
	# Run development server
	python3 manage.py runserver 0.0.0.0:8080

collect_static:
	. .venv/bin/activate && \
	python3 manage.py collectstatic --noinput