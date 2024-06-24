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

format:
	autoflake --remove-all-unused-imports --remove-unused-variables --recursive --in-place . --exclude=__init__.py,venv,.venv;
	black adapters/ api/ core/ factories/
	isort  adapters/ api/ core/ factories/
	flake8  adapters/ api/ core/ factories/