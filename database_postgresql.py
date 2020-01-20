import psycopg2

# 1. Connect to a database
# 2. Create a cursor object
# 3. Write an SQL query
# 4. Commit changes
# 5. Close database connection

def create_table():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='gR00*4Ftyo^Ch^' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

create_table()

def insert(item, quantity, price):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='gR00*4Ftyo^Ch^' host='localhost' port='5432'")
    cur = conn.cursor()
    # below line is vulnerable to SQL injections, 2nd line is not
    # cur.execute("INSERT INTO store VALUES ('%s','%s','%s')" % (item, quantity,price))
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)", (item, quantity,price))
    conn.commit()
    conn.close()

# insert("Water Glass", 10, 5)

def view():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='gR00*4Ftyo^Ch^' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='gR00*4Ftyo^Ch^' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s",(item,))
    conn.commit()
    conn.close()

def update(item, quantity, price):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='gR00*4Ftyo^Ch^' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s",(quantity, price, item))
    conn.commit()
    conn.close()

create_table()
# insert("Wine Glass", 10, 12.50)
# insert("Hand Towel", 50, 5)
# print(view())
# update("Hand Towel", 30, 8.50)


#delete("Water Glass")
# print(view())
