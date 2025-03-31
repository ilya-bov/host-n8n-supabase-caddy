#!/usr/bin/env python
"""
Project management script that provides various utility commands.
Run with `python -m scripts.main [command]` from the project root.
"""

import argparse
import sys
from pathlib import Path

from scripts.generate_env_vars import generate_env_vars
from scripts.update_env import update_env


def init():
    """Initialize the project."""
    print("init")


def start():
    """Start the project."""
    print("start")


def stop():
    """Stop the project."""
    print("stop")


def update():
    """Update the project."""
    print("update")


def reset():
    """Reset the project by deleting all data.
    
    This will remove all data, including databases, containers, and volumes.
    User will be asked to confirm before proceeding.
    """
    import subprocess
    import os
    import time
    
    print("\033[91m" + "WARNING: This will delete ALL data in the project!" + "\033[0m")
    print("This includes:")
    print("- All database data")
    print("- All docker containers")
    print("- All docker volumes")
    print("- Any stored workflows and credentials")
    print("\nThis action CANNOT be undone!")
    
    confirmation = input("To confirm, please type 'DELETE ALL DATA': ").strip()
    
    if confirmation != "DELETE ALL DATA":
        print("Reset cancelled.")
        return
    
    print("Stopping all containers...")
    subprocess.run(["docker", "compose", "down"], check=False)
    
    print("Removing all volumes...")
    # Get a list of volumes associated with the project
    result = subprocess.run(
        ["docker", "volume", "ls", "--filter", "name=n8n", "--quiet"],
        check=True, 
        capture_output=True, 
        text=True
    )
    
    volumes = result.stdout.strip().split('\n')
    volumes = [v for v in volumes if v]  # Remove empty strings
    
    if volumes:
        # Remove each volume
        for volume in volumes:
            print(f"Removing volume: {volume}")
            subprocess.run(["docker", "volume", "rm", volume], check=False)
    
    print("Pruning unused volumes...")
    subprocess.run(["docker", "volume", "prune", "-f"], check=False)
    
    print("All data has been reset. You can now run 'init' to start fresh.")


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(description="Project management commands")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # Register commands
    subparsers.add_parser("generate_env_vars", help="Generate environment variables and print them")
    subparsers.add_parser("update_env", help="Update environment variables")
    subparsers.add_parser("init", help="Initialize the project")
    subparsers.add_parser("start", help="Start the project")
    subparsers.add_parser("stop", help="Stop the project")
    subparsers.add_parser("update", help="Update the project")
    subparsers.add_parser("reset", help="Reset the project by deleting all data")

    args = parser.parse_args()

    # Run the appropriate function based on the command
    if args.command == "generate_env_vars":
        generate_env_vars()
    elif args.command == "update_env":
        update_env()
    elif args.command == "init":
        init()
    elif args.command == "start":
        start()
    elif args.command == "stop":
        stop()
    elif args.command == "update":
        update()
    elif args.command == "reset":
        reset()
    else:
        parser.print_help()
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
