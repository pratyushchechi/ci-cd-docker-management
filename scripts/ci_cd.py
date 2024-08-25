import docker
import os

def remove_container(container_name):
    client = docker.from_env()
    try:
        print(f"Attempting to stop and remove container: {container_name}")
        container = client.containers.get(container_name)
        container.stop()
        container.remove()
        print(f"Removed existing container: {container_name}")
    except docker.errors.NotFound:
        print(f"No container with the name {container_name} was found.")

def create_container(container_name, image_name):
    client = docker.from_env()
    try:
        print(f"Attempting to create and start container: {container_name} from image: {image_name}")
        container = client.containers.run(image_name, name=container_name, detach=True)
        print(f"Created and started container: {container_name}")
    except docker.errors.APIError as e:
        print(f"Failed to create container: {str(e)}")

if __name__ == "__main__":
    container_name = "my_docker_container"
    image_name = "my_docker_image"

    print("Starting CI/CD script...")
    
    # Step 1: Remove the existing container if it exists
    remove_container(container_name)

    # Step 2: Build the Docker image
    print(f"Building Docker image: {image_name}")
    os.system(f"docker build -t {image_name} ./docker")
    
    # Step 3: Create and start the new container
    create_container(container_name, image_name)
    
    print("CI/CD script completed.")

