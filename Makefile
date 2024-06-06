install:
	pip install poetry
	poetry install

create-venv:
	poetry shell
	python3 -m venv .venv
	. .venv/bin/activate;

start-app:
	export PYTHONPATH=$(pwd):$PYTHONPATH
	poetry run uvicorn main:app