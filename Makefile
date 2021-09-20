setup:
	# create a virtual environment and activate it
	python3 -m venv .venv
	source .venv/bin/activate

install:
	# install dependecies
	pip install --upgrade pip &&\
		pip install -r requirements.txt
migrate:
	# run database migrations
	python manage.py makemigrations
	python manage.py migrate
	
lint:
	# run pylint 
	hadolint Dockerfile
	pylint --disable=R,C,W0613,E1101 userreviews/


# TODO: add a symlink creating action to the reviews app: needed for the locale files