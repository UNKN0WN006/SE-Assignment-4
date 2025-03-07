import sqlite3

def connect_db():
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    return conn, c

def create_tables():
    conn, c = connect_db()
    
    # Create Products Table
    c.execute('''CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        brand TEXT,
        quantity INTEGER,
        price REAL)''')
    
    # Create Sales Table
    c.execute('''CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_name TEXT,
        product_id INTEGER,
        quantity INTEGER,
        sale_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (product_id) REFERENCES products (id))''')
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tables()
    print("Database and tables created successfully.")
