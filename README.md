# DIPLOM PROJECT

# Development
1. python3 -m venv .venv
2. source .venv/bin/activate
2. pip install -r requirements.txt

# Make .env file:
- example (.env.template)

# Create DB:
- docker-compose up -d

# Migrations:
- python3 manage.py migrate

# Create Superuser (for admin):
- python3 manage.py createsuperuser

# Run Project:
- python3 manage.py runserver


 
