FROM python:3.10.1-slim-bullseye

ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get clean && \
    rm -rf /var/lib/opt/lists/* && \
    mkdir /code 

WORKDIR /code
COPY ./src ./
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

CMD ["bash", "start_gunicorn.sh"]


