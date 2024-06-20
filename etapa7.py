import sqlite3


class Database:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT UNIQUE,
                password TEXT
            )
        ''')
        self.connection.commit()

    def insert_user(self, username, password):
        self.cursor.execute('''
            INSERT INTO users (username, password) VALUES (?, ?)
        ''', (username, password))
        self.connection.commit()

    def get_user(self, username):
        self.cursor.execute('''
            SELECT * FROM users WHERE username = ?
        ''', (username,))
        return self.cursor.fetchone()

    def close(self):
        self.connection.close()
