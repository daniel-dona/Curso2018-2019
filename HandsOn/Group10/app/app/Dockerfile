FROM ubuntu:latest

RUN apt-get update
RUN apt-get install git python-dev python-pip -y
RUN apt-get install mysql-client libmysqlclient-dev -y

ADD ./entrypoint.sh /
RUN chmod +x /entrypoint.sh

RUN mkdir /opt/bicyparking
WORKDIR /opt/bicyparking

