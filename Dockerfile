FROM python:3.11-slim-bookworm

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /code
COPY . /code/
WORKDIR /code

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
