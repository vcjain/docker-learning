import os
from flask import Flask
import psycopg2

app = Flask(__name__)

def connect_to_db():
    try:
        connection = psycopg2.connect(
            host='db',  # This should match the service name in Docker
            port= os.environ.get('DB_PORT_5432_TCP_PORT'),  # This should match the port exposed by the PostgreSQL container
            user='postgres',
            password='password',  # This should match POSTGRES_PASSWORD in Docker
            database='postgres'  # This should match POSTGRES_DB in Docker
        )
        return connection
    except Exception as e:
        print("Error connecting to PostgreSQL:", e)
        return None

# Define a route
@app.route('/get')
def index():
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute('SELECT * from users')
    result = cursor.fetchone()
    return f'The record is: {result}'

@app.route('/createdb')
def create_database_and_table():
    try:
        # Connect to the database
        connection = connect_to_db()
        if connection is None:
            return "Error connecting to the database"

        # Create a cursor
        cursor = connection.cursor()

        # Create a new database
        #cursor.execute('CREATE DATABASE IF NOT EXISTS my_database')

        # Switch to the new database
        #cursor.execute('USE my_database')

        # Create a new table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL
            )
        ''')
        
        cursor.execute('''
            INSERT INTO users (id , username, email ) VALUES (1, 'vcjain', 'vcjain@self.com')
        ''')

        # Commit the transaction
        connection.commit()

        return "Database and table created successfully"
    except Exception as e:
        return f"Error creating database and table: {e}"
    finally:
        # Close the connection
        if connection is not None:
            connection.close()
# Start the server
if __name__ == '__main__':
    app.run(host='0.0.0.0')
