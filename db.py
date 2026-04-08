import psycopg2
from config import DB_CONFIG


def get_connection():
    conn = psycopg2.connect(
        database=DB_CONFIG["database"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        host=DB_CONFIG["host"],
        port=DB_CONFIG["port"]
    )
    conn.autocommit = True
    return conn
