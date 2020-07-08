FROM python:3

RUN pip install pytest

WORKDIR /app
COPY . .

RUN pytest .
