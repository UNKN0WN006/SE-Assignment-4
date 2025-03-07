import sqlite3
from database_management import connect_db

def add_product(name, brand, quantity, price):
    conn, c = connect_db()
    c.execute("INSERT INTO products (name, brand, quantity, price) VALUES (?, ?, ?, ?)", (name, brand, quantity, price))
    conn.commit()
    conn.close()

def view_products():
    conn, c = connect_db()
    c.execute("SELECT * FROM products")
    products = c.fetchall()
    conn.close()
    return products

def update_product(product_id, new_name, new_brand, new_quantity, new_price):
    conn, c = connect_db()
    c.execute("UPDATE products SET name = ?, brand = ?, quantity = ?, price = ? WHERE id = ?", (new_name, new_brand, new_quantity, new_price, product_id))
    conn.commit()
    conn.close()

def delete_product(product_id):
    conn, c = connect_db()
    c.execute("DELETE FROM products WHERE id = ?", (product_id,))
    conn.commit()
    conn.close()

def search_products(search_term):
    conn, c = connect_db()
    c.execute("SELECT * FROM products WHERE name LIKE ? OR brand LIKE ?", ('%' + search_term + '%', '%' + search_term + '%'))
    results = c.fetchall()
    conn.close()
    return results

def purchase_product(customer_name, product_id, quantity):
    conn, c = connect_db()
    
    c.execute("SELECT quantity, price FROM products WHERE id = ?", (product_id,))
    product = c.fetchone()
    
    if product is None:
        print("Product not found.")
        conn.close()
        return
    
    available_quantity, price = product
    
    if quantity > available_quantity:
        print("Not enough stock available.")
        conn.close()
        return
    
    c.execute("INSERT INTO sales (customer_name, product_id, quantity) VALUES (?, ?, ?)", (customer_name, product_id, quantity))
    c.execute("UPDATE products SET quantity = quantity - ? WHERE id = ?", (quantity, product_id))
    
    conn.commit()
    conn.close()
    
    print("Purchase successful.")
    return price * quantity

def display_products_table(products):
    # Print table headers
    print("{:<5} {:<20} {:<15} {:<10} {:<10}".format("ID", "Name", "Brand", "Quantity", "Price"))
    print("-" * 60)
    
    # Print each product in a formatted row
    for product in products:
        print("{:<5} {:<20} {:<15} {:<10} {:<10}".format(product[0], product[1], product[2], product[3], product[4]))

def display_bill(customer_name, items):
    print("\nCustomer Name: {}".format(customer_name))
    print("{:<5} {:<20} {:<10} {:<10}".format("ID", "Name", "Quantity", "Total Price"))
    print("-" * 50)
    
    total_amount = 0
    for item in items:
        product_id, name, quantity, price = item
        total_price = quantity * price
        total_amount += total_price
        print("{:<5} {:<20} {:<10} {:<10}".format(product_id, name, quantity, total_price))
    
    print("-" * 50)
    print("Total Amount: {:.2f}".format(total_amount))

def main():
    print("Welcome to Inventory Management System")
    
    user_type = raw_input("Enter 'manager' for Product Manager or 'customer' for Customer: ").strip().lower()

    if user_type == 'manager':
        while True:
            action = raw_input("Choose action: add/update/delete/view/exit: ").strip().lower()
            if action == 'add':
                name = raw_input("Enter product name: ")
                brand = raw_input("Enter brand name: ")
                quantity = int(raw_input("Enter quantity: "))
                price = float(raw_input("Enter price: "))
                add_product(name, brand, quantity, price)
                print("Product added.")
            elif action == 'update':
                product_id = int(raw_input("Enter product ID to update: "))
                new_name = raw_input("Enter new product name: ")
                new_brand = raw_input("Enter new brand name: ")
                new_quantity = int(raw_input("Enter new quantity: "))
                new_price = float(raw_input("Enter new price: "))
                update_product(product_id, new_name, new_brand, new_quantity, new_price)
                print("Product updated.")
            elif action == 'delete':
                product_id = int(raw_input("Enter product ID to delete: "))
                delete_product(product_id)
                print("Product deleted.")
            elif action == 'view':
                products = view_products()
                display_products_table(products)
            elif action == 'exit':
                break

    elif user_type == 'customer':
        customer_name = raw_input("Enter your name: ")
        while True:
            action = raw_input("Choose action: search/view/purchase/exit: ").strip().lower()
            if action == 'search':
                search_term = raw_input("Enter product name or brand to search: ")
                results = search_products(search_term)
                display_products_table(results)
            elif action == 'view':
                products = view_products()
                display_products_table(products)
            elif action == 'purchase':
                product_id = int(raw_input("Enter product ID to purchase: "))
                quantity = int(raw_input("Enter quantity to purchase: "))
                total_price = purchase_product(customer_name, product_id, quantity)
                
                # Get product details for the bill
                if total_price:
                    conn, c = connect_db()
                    c.execute("SELECT name, price FROM products WHERE id = ?", (product_id,))
                    product = c.fetchone()
                    conn.close()
                    
                    if product:
                        items = [(product_id, product[0], quantity, product[1])]
                        display_bill(customer_name, items)  # Display the bill
            elif action == 'exit':
                break

if __name__ == "__main__":
    #from databasemanagement import create_tables
    #create_tables() # Ensure tables are created when app starts
    main()
