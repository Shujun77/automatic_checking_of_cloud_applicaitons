FROM nestybox/ubuntu-bionic-docker:latest

WORKDIR /workspace
VOLUME /workspace

COPY . .
RUN apt-get update && \
      apt-get -y install sudo

RUN echo "ALL ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

RUN apt-get install python3 -y
RUN apt-get install python3-pip -y && pip3 install --upgrade pip 
RUN pip3 install docker

RUN curl -L "https://github.com/docker/compose/releases/download/1.24.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose && \
    chmod +x /usr/local/bin/docker-compose

CMD service docker start ; python3 /workspace/AutoTest.py