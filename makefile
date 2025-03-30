.PHONY: log-env

# Log environment variables
generate-env:
	@echo "POSTGRES_USER=postgres"
	@echo "POSTGRES_PASSWORD=$$(openssl rand -base64 16 | tr -dc 'a-zA-Z0-9' | head -c 16)"
	@echo "POSTGRES_DB=postgres"
	@echo ""
	@echo "N8N_ENCRYPTION_KEY=$$(openssl rand -hex 16)"
	@echo "N8N_USER_MANAGEMENT_JWT_SECRET=$$(openssl rand -hex 32)"
