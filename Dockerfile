FROM python:3.6.8-slim
MAINTAINER Oliver Rice <oliver@truepic.com>

RUN apt-get update && \
    apt-get install -y libopenblas-dev gfortran

COPY server.py setup.py /

RUN pip3.6 install -e ".[prod]"


EXPOSE 80
ENV PORT=80 \
    WORKER_COUNT=4 \
    ELASTICSEARCH_URL=https://vpc-match-hmyezdubn6xpxprx5txxrfopde.us-east-1.es.amazonaws.com \
    ELASTICSEARCH_INDEX=images \
    ELASTICSEARCH_DOC_TYPE=images \
    ALL_ORIENTATIONS=true

CMD gunicorn \
    -t 60 \
    --access-logfile - \
    --access-logformat '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" - %(D)s' \
    -b 0.0.0.0:${PORT} \
    -w ${WORKER_COUNT} \
    server:app
