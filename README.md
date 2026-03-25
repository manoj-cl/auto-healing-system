# METHOD 1
# Run this project using below command
docker run -d --name <image_name> -v $(pwd)/logs:/app/logs <container_name>

# WHAT THIS DOES
$(pwd)/logs   → your Mac folder
/app/logs     → container folder
Now they are connected.

image_name: auto-healer
container_name: auto-healer

# METHOD 2
# Run below command which makes use of docker-compose.yaml file to perform the same operation as above command
docker compose up
