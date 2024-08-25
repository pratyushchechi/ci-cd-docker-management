# CI/CD Docker Management Script

This project automates the management of Docker containers using a Python script in a CI/CD pipeline. The script:
1. Stops and removes any running Docker container with a specified name.
2. Builds a Docker image using a provided `Dockerfile`.
3. Creates and starts a new Docker container with the updated image.


## Prerequisites

- Python 3.x
- Docker installed and running
- Git

## Setup Instructions

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/pratyushchechi/ci-cd-docker-management.git
   cd ci-cd-docker-management

2. **Create a Virtual Environment:**

    ```bash
    python3 -m venv venv


3. **Activate the Virtual environment:

  ```bash

    source venv/bin/activate

4. Install Dependencies:
  ```bash
    pip install -r requirements.txt


## Usage
1. ** Run the CI/CD Python Script:
  
    ```bash
    python3 scripts/ci_cd.py

2. ** Access the web page:**
 
      Open your web browser and navigate to http://<your-ec2-public-ip> to view the HTML page served by the Docker container.

# Troubleshooting
If you encounter issues with Docker permissions, you can try the following:

Run the script with sudo.
Add your user to the Docker group with: sudo usermod -aG docker $USER, then log out and log back in.
    
