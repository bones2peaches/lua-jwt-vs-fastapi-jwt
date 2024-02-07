import psycopg2
from psycopg2 import OperationalError
import sys
from .get_url import dbname , user , password , host , port
import logging
def check_postgres():
    try:
        # Connect to your postgres DB
        conn = psycopg2.connect(
            dbname=dbname,  # Replace with your DB name
            user=user,  # Replace with your username
            password=password,  # Replace with your password
            host=host,  # Replace with your host, use "postgres" if running in Docker Compose
            port=port  # Replace with your port, "5432" is the default
        )

        # Open a cursor to perform database operations
        cur = conn.cursor()

        # Execute a query
        cur.execute("SELECT 1")

        # Fetch result
        cur.fetchone()

        # Close the cursor and connection
        cur.close()
        conn.close()

        logging.info("PostgreSQL is up and running.")
        return True

    except OperationalError as e:
        logging.error(f"PostgreSQL connection failed: {e}")
        return False