FROM python:3.11.3-slim

WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
RUN apt-get update && apt-get install nano -y && apt-get install curl -y

COPY ./requirements.txt .
RUN pip install -r requirements.txt


# copy project
COPY . .
# create logs directory
RUN mkdir -p logs

#COPY ./static /var/static
RUN python manage.py collectstatic --no-input

CMD gunicorn -b 0.0.0.0:$GUNICORN_PORT spk_notifications.wsgi --workers 2 --timeout 600