FROM python:3.6-slim

COPY . /root

WORKDIR /root

RUN pip install flask gunicorn numpy sklearn flask_wtf pandas nltk
# FROM python:2.7-slim

# RUN apt-get update && apt-get install -qq -y \
#   build-essential libpq-dev --no-install-recommends

# ENV INSTALL_PATH /web_app
# RUN mkdir -p $INSTALL_PATH

# WORKDIR $INSTALL_PATH

# COPY requirements.txt requirements.txt
# RUN pip install -r requirements.txt

# COPY . .

# CMD gunicorn -b 0.0.0.0:8000 --access-logfile - "web_app.app:app"