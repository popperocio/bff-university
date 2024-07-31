FROM python:3.9.14

WORKDIR /app

RUN apt-get update && apt-get install -y curl

COPY poetry.lock /app
COPY pyproject.toml /app

RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry install 

COPY main.py /app
COPY api /app/api
COPY core /app/core
COPY factories /app/factories
COPY adapters /app/adapters
COPY setup.cfg /app/setup.cfg
COPY conftest.py /app/conftest.py

CMD [ "poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]