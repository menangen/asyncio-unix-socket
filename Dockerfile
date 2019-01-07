FROM python:alpine

MAINTAINER Menangen <menangen@gmail.com>

WORKDIR /opt/app/

COPY *.py /opt/app/

VOLUME ["/tmp"]

CMD [ "python", "server.py" ]