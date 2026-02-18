import sqlite3
def login(username, password):
    conn = sqlite3.connect("db.sqlite")
    query = "SELECT * FROM users WHERE user='" + username + "' AND pass='" + password + "'"
    return conn.execute(query).fetchone()

