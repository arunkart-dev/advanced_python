from db import get_connection


def add_product(pname, pdescription, price):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO ECOMM(pname,pdescription,price) VALUES (%s,%s,%s)",
        (pname,pdescription,price)
    )
    conn.commit()
    conn.close()

    print("Product added !!")


def view_product():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM ECOMM"
    )

    rows = cur.fetchall()

    for r in rows:
        print(r)

    conn.close()


def update_product(pid,price):

    conn = get_connection()
    cur = conn.cursor()

    print("PID:", pid, type(pid))
    print("PRICE:", price, type(price))

    cur.execute(
        "UPDATE public.ECOMM SET price=%s WHERE id=%s",
        (price,pid)
    )

    conn.commit()
    print("Rows affected",cur.rowcount)
    conn.close()

    print("Product updated !!")


def delete_product(pid):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM ECOMM WHERE id=%s",
        (pid,)
    )

    conn.commit()
    conn.close()



