# AI Project Base

This repository serves as a foundational setup for AI projects, enabling seamless local development and deployment to an Apptainer (formerly Singularity) cluster. It includes essential configurations, dependencies, and scripts to streamline your AI development workflow.

## Features

- **Local Development**: Use Docker to create a consistent development environment.
- **Cluster Deployment**: Utilize Apptainer for deploying your projects to a high-performance computing (HPC) cluster.
- **Essential Dependencies**: Pre-configured with common AI/ML libraries and tools.
- **Easy Setup**: Simplified setup process for both local and cluster environments.

## Prerequisites

Ensure you have the following installed on your local machine:

- Docker
- Git

For Windows users, it is recommended to set up Windows Subsystem for Linux (WSL) to run CUDA virtually. Please refer to the following resources to set up WSL and enable CUDA:

- [Microsoft WSL Installation Guide](https://docs.microsoft.com/en-us/windows/wsl/install)
- [NVIDIA CUDA on WSL](https://docs.nvidia.com/cuda/wsl-user-guide/index.html)

## Installation

### Local Development with Docker

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/nachtflug6/PytorchProjectBase.git
   cd PytorchProjectBase

2. **Build the Docker Image**:
    ```bash
    docker build -t PytorchProjectBase:latest -f Dockerfile .

3. **Run the Docker Container**:
    ```bash
    docker run -it --rm -p 8888:8888 -v $(pwd):/workspace PytorchProjectBase:latest

4. **Access Jupyter Notebook**:
    Open your browser and navigate to http://localhost:8888 to access the Jupyter Notebook interface.

### Check

1. **Check if CUDA is available and installation successful**:
    ```bash
    python main.py

## Cluster Deployment with Apptainer

1. **Build the Apptainer Image**:
    ```bash
    apptainer build PytorchProjectBase.sif Dockerfile_apptainer.def

2. **Run the Apptainer Container**:
    ```bash
    apptainer run PytorchProjectBase.sif

