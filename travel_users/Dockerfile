FROM python:3.9.16-alpine3.17
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY /requirements.txt /app/requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
COPY .. /app
