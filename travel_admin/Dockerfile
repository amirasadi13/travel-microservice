# syntax=docker/dockerfile:1
FROM python:3.9.16-alpine3.17
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN python3 -m pip install --upgrade pip
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY .. /app/