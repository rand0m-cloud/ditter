FROM python:3.11-alpine

WORKDIR /app

ADD requirements.txt /app
RUN pip install --requirement requirements.txt

CMD sh -c "python manage.py migrate --no-input && python manage.py runserver 0.0.0.0:8000"