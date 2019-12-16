FROM python:3
WORKDIR usr/src/app

WORKDIR /usr/src/app

ENV DJANGO_PROJECT_NAME=teste

ADD . ${BASE_FOLDER}

ADD supervisor.conf  /etc/supervisord.conf


RUN pip3 install -r requirements.txt

RUN chmod +x run.sh

RUN apt update && apt install supervisor -y

EXPOSE 8000

CMD ./run.sh