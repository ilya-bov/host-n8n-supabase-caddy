"""
Generate secure environment variables for n8n setup.
"""

import base64
import secrets


def generate_env_vars():
    """Generate environment variables.
    
    Returns:
        dict: Dictionary of generated environment variables
    """
    # Function to generate a secure random string
    def generate_secure_key(bytes_length=32):
        return base64.urlsafe_b64encode(secrets.token_bytes(bytes_length)).decode('ascii').rstrip('=')
    
    # Generate secure values
    n8n_postgres_password = generate_secure_key(24)
    n8n_encryption_key = generate_secure_key(32)
    n8n_user_management_jwt_secret = generate_secure_key(48)
    
    # Create environment variables dictionary
    env_vars = {
        "N8N_POSTGRES_PASSWORD": n8n_postgres_password,
        "N8N_ENCRYPTION_KEY": n8n_encryption_key,
        "N8N_USER_MANAGEMENT_JWT_SECRET": n8n_user_management_jwt_secret
    }
    print("Generated the following variables:")
    for key, value in env_vars.items():
        print(f"- {key}: {value}")
    
    return env_vars


if __name__ == "__main__":
    # Allow this file to be run directly for testing
    generate_env_vars() 