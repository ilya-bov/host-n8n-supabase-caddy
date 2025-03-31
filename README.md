# Environment Setup Scripts

Scripts to generate secure environment variables for Supabase and n8n setup.

## Setup

1. Create Python virtual environment:
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the script:
```bash
python scripts/generate_env_vars.py
```

## Requirements
- Python 3.7 or higher