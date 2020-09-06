FROM python:3.6

ARG pdir=/projects/

ADD requirements.txt $pdir

ADD pub.py $pdir

WORKDIR $pdir

RUN pip install -r requirements.txt
