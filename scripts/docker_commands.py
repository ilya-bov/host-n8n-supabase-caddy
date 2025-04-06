from scripts.utils import run_command

def start():
    """Start the project."""
    # Start Supabase services with project name
    print("Starting Supabase...")
    run_command([
        "docker", "compose",
        "-f", "supabase/docker/docker-compose.yml",
        "-p", "${PROJECT_NAME}_supabase",
        "up", "-d"
    ])

    # Start n8n services with project name
    print("Starting n8n...")
    run_command([
        "docker", "compose",
        "-p", "${PROJECT_NAME}_n8n",
        "up", "-d"
    ])

    print("\nServices started!")
    print("- n8n: http://localhost:5678")
    print("- Supabase Dashboard: http://localhost:8000")
    print("- Supabase Inside N8N: http://host.docker.internal:8000")


def stop():
    """Stop the project."""
    print("Stopping n8n services...")
    run_command([
        "docker", "compose",
        "-p", "${PROJECT_NAME}_n8n",
        "down"
    ], ignore_errors=True)

    print("Stopping Supabase services...")
    run_command([
        "docker", "compose",
        "-f", "supabase/docker/docker-compose.yml",
        "-p", "${PROJECT_NAME}_supabase",
        "down"
    ], ignore_errors=True)

    print("\nAll services stopped!") 