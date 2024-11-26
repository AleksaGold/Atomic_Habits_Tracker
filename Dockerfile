FROM python:3.12-slim

WORKDIR /habits

COPY pyproject.toml poetry.lock ./

RUN pip install poetry && \
    poetry config virtualenvs.create false &&  \
    poetry install --no-dev

COPY . .
