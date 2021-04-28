import os
import subprocess
import docker
import time

docker_project_path = './studentCode'

# url = "http://localhost:8001/"
# Linux curl url
# url = "http://host.docker.internal:8001/"
# mac curl url
url = "http://docker.for.mac.localhost:8001/"


def get_docker_needed_files(dir_name):
    dockerfile_list, docker_compose_path = [], ""
    for root, dirs, files in os.walk(dir_name):
        for filename in files:
            if filename.lower() == "dockerfile" or os.path.splitext(filename)[-1] == ".dockerfile":
                dockerfile_list.append(root)
            if filename == "docker-compose.yml":
                docker_compose_path = root
                return [],docker_compose_path
    return dockerfile_list, docker_compose_path
    

def docker_subprocess_popen(statement, homework_path):
    try:
        if os.path.exists(homework_path + '/docker-compose.yml'):
            subprocess_popen(statement, homework_path)
        else:
            print("docker-compose.yml doesn't exist")
            return False
    except Exception as e:
        print(e)

def subprocess_popen(statement, homework_path):
    p = subprocess.Popen(statement, shell=True, stdout=subprocess.PIPE, cwd=homework_path)
    while p.poll() is None:  # check if the process is stopped
        if p.wait() != 0:  # check if the process is running successful
            print(" Execution failed, please check the containers connection status")
            return False
        else:
            re = p.stdout.readlines()  # Get the raw execution result
            result = []
            for i in range(len(re)):
                res = re[i].decode('utf-8').strip('\r\n')
                result.append(res)
            return result

client = docker.from_env()

dockerfile_list, docker_compose_path = get_docker_needed_files(docker_project_path)
 
if docker_compose_path:
    subprocess_popen("sudo docker-compose --compatibility up -d", docker_compose_path)
    
    # time.sleep(10)

    print(subprocess_popen("sudo docker ps | tee log.log", docker_compose_path))
    print(subprocess_popen("curl {curl_url} | tee result.log".format(curl_url=url), docker_compose_path))

    time.sleep(5)
    subprocess_popen("sudo docker-compose down", docker_compose_path)
    
elif dockerfile_list:
    for dockerfile_path in dockerfile_list:
        # build image
        image, logs_list = client.images.build(path=dockerfile_path, rm=True, nocache=True)

        for logs in logs_list:
            print(logs)
