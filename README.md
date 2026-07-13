# START THE CONTAINER

### METHOD 1
Run this project using below command. 
```
docker run -d --name <image_name> -v $(pwd)/logs:/app/logs <container_name>
```
**WHAT THIS DOES** \
$(pwd)/logs   → your Mac folder \
/app/logs     → container folder \
Now they are connected.  

Provide the values as:  
<image_name> -> auto-healer \
<container_name> -> auto-healer

### METHOD 2
Run below command which makes use of docker-compose.yaml file to perform the same operation as above command. 
```
docker compose up
```

# STRESS TEST
Run below command to enter the bash command-line of the container:
```
docker exec -it <container-name> bash
```
Run below command to initiate the stress to increase CPU and memory load on the container:
```
python /app/stress_test.py
```