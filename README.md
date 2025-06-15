# N8N Supabase Local Development Setup

This project helps you set up a local development environment with N8N and Supabase using Docker.

## Inspiration

This project was inspired by:
- [local-ai-packaged](https://github.com/coleam00/local-ai-packaged)
- [n8n-io/self-hosted-ai-starter-kit](https://github.com/n8n-io/self-hosted-ai-starter-kit)

While these projects are excellent, I didn't want to run the LLM locally and I needed something simpler that would allow me to:
- Quickly start and stop the services
- Generate new environment variables easily
- Manage local development without complexity

## Requirements

The project requires:
- Python 3.6+
- Docker
- Docker Compose
- Git


## Prerequisites

### 1. Git
- **Windows**: Download and install from [Git for Windows](https://gitforwindows.org/)
- **macOS**:
  ```bash
  # If you don't have brew see https://brew.sh/
  brew install git
  ```
- **Linux**:
  ```bash
  sudo apt update
  sudo apt install git
  ```

After installation, configure your Git identity:
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### 2. Python (3.6 or higher)
- **Windows**: Download from [Python.org](https://www.python.org/downloads/)
- **macOS**: 
  ```bash
  brew install python
  ```
- **Linux**:
  ```bash
  sudo apt update
  sudo apt install python3 python3-pip
  ```

### 2. Docker
- Download and install [Docker Desktop](https://www.docker.com/products/docker-desktop)

## Setup

1. **Clone the repository**


   ```cmd
   git clone -b stable https://github.com/ilya-bov/host-n8n-supabase-caddy.git
   cd host-n8n-supabase-caddy
   ```

3. **Create and activate virtual environment**
   
   Windows:
   ```cmd
   python -m venv venv
   .\venv\Scripts\activate
   ```

   macOS/Linux:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

All commands should be run from the project root directory with the virtual environment activated.

### Available Commands

1. **Initialize the project**
   ```bash
   python -m script init
   ```
   This will:
   - Create necessary environment files
   - Clone and set up Supabase
   - Configure the environment

2. **Start the services**
   ```bash
   python -m script start
   ```
   This starts both N8N and Supabase services.

3. **Stop the services**
   ```bash
   python -m script stop
   ```
   This stops all running containers.

4. **Update environment variables**
   ```bash
   python -m script update_env
   ```
   Updates the environment variables in both N8N and Supabase.

5. **Generate new environment variables**
   ```bash
   python -m script generate_env_vars
   ```
   Generates new secure environment variables.

6. **Reset the project**
   ```bash
   python -m script reset
   ```
   ⚠️ WARNING: This will delete all data, including:
   - All database data
   - All docker containers
   - All docker volumes
   - All Supabase data and containers
   - Any stored workflows and credentials

### Accessing Services

After starting the services, you can access:
- N8N: http://localhost:5678
- Supabase Dashboard: http://localhost:8000
- Supabase URL from within N8N: http://host.docker.internal:8000

## Troubleshooting

1. **Docker not running**
   - Ensure Docker Desktop is running (Windows/macOS)
   - On Linux, check Docker service: `sudo systemctl status docker`

2. **Port conflicts**
   - Ensure ports 5678 (N8N) and 8000 (Supabase) are not in use
   - Stop any existing containers: `python -m script stop`

3. **Permission issues**
   - Windows: Run terminal as Administrator
   - Linux: Ensure your user is in the docker group or use sudo

4. **Virtual environment issues**
   - If `venv` activation fails, ensure Python is properly installed
   - Try removing and recreating the virtual environment
