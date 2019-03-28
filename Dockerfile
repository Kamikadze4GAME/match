FROM python:3.6.8-slim
MAINTAINER Oliver Rice <oliver@truepic.com>

RUN apt-get update && \
    apt-get install -y libopenblas-dev gfortran

WORKDIR /app

ADD src /app/src
COPY setup.py /app/

RUN pip3.6 install numpy
RUN pip3.6 install -e .


ENV PORT=80 \
    ELASTICSEARCH_URL=http://localhost:9200 \
    WORKER_COUNT=4 \
    ELASTICSEARCH_INDEX=images \
    ELASTICSEARCH_DOC_TYPE=images \
    ALL_ORIENTATIONS=true


EXPOSE 80

CMD gunicorn \
    -t 60 \
    --access-logfile - \
    --access-logformat '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" - %(D)s' \
    -b 0.0.0.0:${PORT} \
    -w ${WORKER_COUNT} \
    app:app
