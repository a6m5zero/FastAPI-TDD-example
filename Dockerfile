FROM python:3.10.1-slim-buster
RUN mkdir -p /usr/src/project/app
WORKDIR /usr/src/project

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get -y install netcat gcc \
    && apt-get clean

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN chmod +x /usr/src/project/entrypoint.sh

ENTRYPOINT ["/usr/src/project/entrypoint.sh"]