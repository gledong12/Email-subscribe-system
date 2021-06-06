FROM python:3.9.1

MAINTAINER Backend Developer DONG

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /usr/src//Email_Subscribe/

WORKDIR /usr/src//Email_Subscribe

RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/Email_Subscribe
EXPOSE 8000