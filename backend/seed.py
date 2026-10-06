import sqlite3
import os

DB_PATH = 'jaymani.db'

def setup_db():
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    
    conn = sqlite3.connect(DB_PATH)
    
    conn.executescript('''
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL,
            location TEXT
        );
        
        CREATE TABLE products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT,
            price REAL NOT NULL,
            stock INTEGER NOT NULL,
            vendor_id INTEGER,
            image TEXT,
            description TEXT,
            FOREIGN KEY(vendor_id) REFERENCES users(id)
        );
        
        CREATE TABLE orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            farmer_id INTEGER,
            vendor_id INTEGER,
            total REAL,
            status TEXT,
            date TEXT,
            FOREIGN KEY(farmer_id) REFERENCES users(id),
            FOREIGN KEY(vendor_id) REFERENCES users(id)
        );
    ''')
    
    # Insert Demo Data
    conn.execute("INSERT INTO users (name, email, password, role, location) VALUES ('Admin Demo', 'admin@jaymani.com', 'admin123', 'admin', 'Head Office')")
    conn.execute("INSERT INTO users (name, email, password, role, location) VALUES ('Ramesh Farmer', 'farmer@jaymani.com', 'farmer123', 'farmer', 'Village A')")
    conn.execute("INSERT INTO users (name, email, password, role, location) VALUES ('Suresh Vendor', 'vendor@jaymani.com', 'vendor123', 'vendor', 'Market B')")
    
    conn.execute("INSERT INTO products (name, category, price, stock, vendor_id, description) VALUES ('Urea Fertilizer 50kg', 'Fertilizer', 1200, 50, 3, 'High quality urea for crops')")
    conn.execute("INSERT INTO products (name, category, price, stock, vendor_id, description) VALUES ('Wheat Seeds (Premium)', 'Seeds', 800, 100, 3, 'High yield wheat seeds')")
    
    conn.commit()
    conn.close()
    print("Database jaymani.db created and seeded successfully!")

if __name__ == '__main__':
    setup_db()
