FROM python:3.10-alpine

RUN mkdir -p /home/jenkinsapp

COPY . /home/jenkinsapp