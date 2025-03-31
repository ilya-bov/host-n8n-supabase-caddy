"""
Update environment variables by copying from .env.example and updating with secure values.
"""

import os
import re
import sys
import shutil
from pathlib import Path
from datetime import datetime

# Import the generate_env_vars function
from scripts.generate_env_vars import generate_env_vars


def update_env():
    """Update environment variables.
    
    - Always copies from .env.example to .env (after confirmation if .env exists)
    - Generates new secure variables and updates them in .env
    
    Returns:
        dict: Dictionary of updated environment variables or None if operation canceled
    """
    env_path = Path(".env")
    env_example_path = Path(".env.example")
    
    # Check if .env.example exists
    if not env_example_path.exists():
        print("Error: .env.example file not found")
        print("Please create an .env.example file first")
        return None
    
    # If .env already exists, ask for confirmation and create backup
    if env_path.exists():
        # Ask for confirmation
        print("Warning: .env file already exists")
        print("Updating environment variables may impact access to the database")
        confirmation = input("Do you want to continue? (y/N): ").strip().lower()
        
        if confirmation != 'y':
            print("Operation canceled")
            return None
        
        # Create backup of current .env
        backup_path = Path(f".env.backup.{datetime.now().strftime('%Y%m%d%H%M%S')}")
        shutil.copy2(env_path, backup_path)
        print(f"Created backup of .env at {backup_path}")
    
    # Always copy .env.example to .env
    print(f"Copying .env.example to .env")
    shutil.copy2(env_example_path, env_path)
    
    # Generate new environment variables
    new_vars = generate_env_vars()
    
    # Read current .env content (which is now from .env.example)
    with open(env_path, 'r') as f:
        env_content = f.read()
    
    # Update or add new variables to .env
    for key, value in new_vars.items():
        # Check if the variable already exists in the file
        pattern = re.compile(f"^{re.escape(key)}=.*$", re.MULTILINE)
        if pattern.search(env_content):
            # Replace existing variable
            env_content = pattern.sub(f"{key}={value}", env_content)
            print(f"Updated {key} in .env")
        else:
            # Add new variable
            if env_content and not env_content.endswith('\n'):
                env_content += '\n'
            env_content += f"{key}={value}\n"
            print(f"Added {key} to .env")
    
    # Write updated content back to .env
    with open(env_path, 'w') as f:
        f.write(env_content)
    
    print(f"Environment variables updated in {env_path}")
    return new_vars


if __name__ == "__main__":
    # Allow this file to be run directly for testing
    update_env()