FROM python:3.11-alpine

WORKDIR /app
ADD . /app

RUN pip install --requirement requirements.txt

RUN python3 manage.py collectstatic --noinput
RUN apk add nginx

ENTRYPOINT /bin/sh -c "python3 manage.py migrate; nginx; gunicorn --access-logfile - --workers 3 --bind 0.0.0.0:9000 ditter.wsgi:application "