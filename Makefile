install:
		poetry install

dev:
		poetry run flask --app magic_ball:app run --debug

PORT ?= 8000
start:
		poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) magic_ball:app

lint:
		poetry run flake8 magic_ball

clean-sessions:
		rm -r flask_session