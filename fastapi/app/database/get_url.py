import os

dbname = os.getenv('DB_NAME')
user = os.getenv('DB_USER')  
password = os.getenv('DB_PASSWORD') 
host = os.getenv('DB_HOST')  
port = os.getenv('DB_PORT')  


postgres_url = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"

