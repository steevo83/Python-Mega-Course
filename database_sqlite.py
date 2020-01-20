import sqlite3

# 1. Connect to a database
# 2. Create a cursor object
# 3. Write an SQL query
# 4. Commit changes
# 5. Close database connection

def create_table():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item, qty, price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (?,?,?)", (item, qty, price))
    conn.commit()
    conn.close()

# insert("Water Glass", 10, 5)

def view():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,))
    conn.commit()
    conn.close()

def update(item, qty, price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?",(qty, price, item))
    conn.commit()
    conn.close()

insert("Wine Glass", 10, 12.50)
insert("Hand Towel", 50, 5)
print(view())
update("Hand Towel", 30, 8.50)


#delete("Water Glass")
print(view())
