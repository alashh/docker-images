FROM python:3.6-alpine

WORKDIR /root

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN mkdir .aws
COPY ./awsconfig  .aws/config
COPY ./awscred  .aws/credentials

RUN mkdir scripts

LABEL maintainer="Adam Lash <Adam.Lashh@gmail.com>" \
      version="17.11"

CMD sh
