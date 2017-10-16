FROM python:3.6
MAINTAINER "seanbl@me.com"

# Copy requirements file in seperately to rest of project.
# This allows docker to cache requirements, and so only changes to
# requirements.txt will trigger a new pip install
ADD requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

ADD . /ahl-example
WORKDIR /ahl-example

ENV PYTHONPATH=/ahl-example:$PYTHONPATH
