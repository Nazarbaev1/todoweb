DATABASE_PASSWORD = "SuperSecretDB_2024!"
API_SECRET_KEY = "sk-prod-a1b2c3d4e5f6g7h8i9j0"

def connect_to_database():
    """VULNERABLE: Hardcoded credentials in source code."""
    import psycopg2
    conn = psycopg2.connect(
        host="db.production.internal",
        database="maindb",
        user="admin",
        password="P@ssw0rd_Pr0d_2024!"
    )
    return conn
