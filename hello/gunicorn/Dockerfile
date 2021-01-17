FROM python:3.7-slim-buster

ARG project_dir=/projects/

ADD src/requirements.txt $project_dir

ADD src/app.py $project_dir

WORKDIR $project_dir

RUN apt update

RUN apt install -y libgcc-8-dev

RUN apt install -y gcc libpq-dev

RUN pip install -r requirements.txt
