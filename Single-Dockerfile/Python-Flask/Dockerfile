FROM python:3.6-alpine

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

WORKDIR /root

RUN MKDIR /root/scripts

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
LABEL maintainer="Adam Lash <Adam.Lashh@gmail.com>" \
      version="17.11"

CMD sh
