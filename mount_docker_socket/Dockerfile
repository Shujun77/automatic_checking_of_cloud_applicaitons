FROM python:3.9-alpine

WORKDIR /Users/shujunliu/Desktop/thesis/workspace 
VOLUME /Users/shujunliu/Desktop/thesis/workspace 

RUN apk --no-cache add curl

# RUN pip3 install -r requirements.txt
RUN pip install docker

# COPY . .
# RUN pip install 'docker-compose==1.8.0'
COPY ./workspace/AutoTest.py /workspace/AutoTest.py
COPY --from=library/docker:latest /usr/local/bin/docker /usr/bin/docker
COPY --from=docker/compose:latest /usr/local/bin/docker-compose /usr/bin/docker-compose