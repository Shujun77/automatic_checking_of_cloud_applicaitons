FROM docker:dind

USER root

# mac needed requirement 
WORKDIR /Users/shujunliu/Desktop/dind/workspace 
VOLUME /Users/shujunliu/Desktop/dind/workspace 

# Linux needed requirement 
WORKDIR /workspace 
VOLUME /workspace 

COPY ./workspace /workspace

RUN apk add --no-cache curl
RUN set -ex && apk --no-cache add sudo

RUN echo "ALL ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

RUN apk add --update python3 py3-pip python3-dev
RUN pip3 install docker

COPY --from=docker/compose:latest /usr/local/bin/docker-compose /usr/bin/docker-compose

