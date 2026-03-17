import sqlite3
import sqlite_vec
from os import path

DB_PATH = "college_project.db"

class Database:
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        
        self.conn.enable_load_extension(True)
        sqlite_vec.load(self.conn)
        self.conn.enable_load_extension(False)
        
        self.conn.execute("PRAGMA foreign_keys = ON;")
        
        self._create_tables()

    def _create_tables(self):
        sql_path = path.join('db','database.sql')
        with open(sql_path, 'r') as f:
            sql = f.read()
        with self.conn:
            self.conn.executescript(sql)

    def execute(self, query, params=()):
        with self.conn:
            cursor = self.conn.execute(query, params)
            self.conn.commit()
            return cursor

    def query(self, query, params=()):
        cursor = self.conn.execute(query, params)
        return cursor.fetchall()

db = Database()