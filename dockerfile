FROM python:3.11-alpine

ENV PYTHONUNBUFFERED 1

RUN mkdir /keycloak
WORKDIR /keycloak

RUN apk --no-cache add \
     bash \
     curl \
     gcc \
     git \
     linux-headers \
     build-base

RUN apk add --no-cache python3-dev openssl-dev py3-setuptools && pip3 install --upgrade pip

COPY requirements.txt /keycloak
RUN pip install -r requirements.txt


COPY . /keycloak

WORKDIR keycloak
