FROM python:3.8-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y iputils-ping \
    && apt-get install -y default-libmysqlclient-dev build-essential \
 && rm -rf /var/lib/apt/lists/*
 
RUN mkdir /challenge_project 
WORKDIR /challenge_project

COPY requirements.txt /challenge_project/
RUN pip install --upgrade pip==23.0.1

RUN pip install -r requirements.txt

COPY . /challenge_project/