import psycopg2

try:
    conn = psycopg2.connect(
        database = "ecomm",
        user = "postgres",
        password = "karthik",
        host = "127.0.0.1",
        port = "5432"
    )
    print("Connected to database !!!")
    conn.close()
except Exception as e:
    print("Connection failed : ",e)
