# DIPLOM PROJECT

# Development
1. python3 -m venv .venv
2. source .venv/bin/activate
3. pip install -r requirements.txt
4. sudo apt install make

# Make .env file:
- example (.env.template)

# Create DB
- docker-compose up -d

# Migrations and RUN:
- make load_db

info: createsuperuser 
			- email:    admin@admin.org
			- password: admin
			- password: admin
			- "y" 



