from scripts.utils import run_command

def start():
    """Start the project."""
    # Start Supabase services
    print("Starting Supabase...")
    run_command([
        "docker", "compose",
        "-f", "supabase/docker/docker-compose.yml",
        "up", "-d"
    ])

    # Start n8n services
    print("Starting n8n...")
    run_command([
        "docker", "compose",
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
        "down"
    ], ignore_errors=True)

    print("Stopping Supabase services...")
    run_command([
        "docker", "compose",
        "-f", "supabase/docker/docker-compose.yml",
        "down"
    ], ignore_errors=True)

    print("\nAll services stopped!") 