FROM docker.elastic.co/logstash/logstash:8.4.2
USER root
RUN mkdir -p /usr/share/logstash/pipeline
RUN mkdir -p /java_driver

COPY ./driver /java_driver
COPY ./logstash-configuration /usr/share/logstash/pipeline
