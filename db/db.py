import os
import psycopg2
from psycopg2.extras import RealDictCursor
from pgvector.psycopg2 import register_vector
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Database:
    def __init__(self):
        # Retrieve the Neon connection string from environment
        self.db_url = os.getenv("DATABASE_URL")
        
        # Connect to Neon
        self.conn = psycopg2.connect(self.db_url)
        self.conn.autocommit = True
        
        # Enable pgvector in this connection
        with self.conn.cursor() as cur:
            cur.execute("CREATE EXTENSION IF NOT EXISTS vector;")
            register_vector(self.conn)
        
        self._create_tables()

    def _create_tables(self):
        # Ensure the path points to your updated Postgres SQL file
        sql_path = os.path.join('db', 'database.sql')
        if os.path.exists(sql_path):
            with open(sql_path, 'r') as f:
                sql = f.read()
            with self.conn.cursor() as cur:
                cur.execute(sql)

    def execute(self, query, params=()):
        with self.conn.cursor() as cur:
            cur.execute(query, params)
            return cur

    def query(self, query, params=()):
        # RealDictCursor makes results behave like sqlite3.Row (accessible by column name)
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(query, params)
            return cur.fetchall()

# Initialize the database instance
db = Database()