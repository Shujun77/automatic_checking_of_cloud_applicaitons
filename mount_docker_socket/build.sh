docker build -t autotest:latest . --no-cache
docker-compose up --build



sudo docker container prune

sudo docker network ls
sudo docker network inspect bridge
sudo docker network inspect message_queue_network
sudo docker network inspect thesis_default

sudo docker attach --sig-proxy=false httpserver
docker container inspect httpserver | grep HostPort