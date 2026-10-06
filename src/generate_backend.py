import os
import subprocess

def create_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

# =======================
# BACKEND (FLASK + SQLITE)
# =======================
backend_dir = 'backend'

app_py = """from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import os
import datetime

app = Flask(__name__)
CORS(app)
DB_PATH = 'jaymani.db'

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api/auth/login', methods=['POST'])
def login():
    data = request.json
    conn = get_db()
    user = conn.execute('SELECT * FROM users WHERE email = ? AND password = ?', (data['email'], data['password'])).fetchone()
    if user:
        return jsonify(dict(user))
    return jsonify({'error': 'Invalid credentials'}), 401

@app.route('/api/products', methods=['GET'])
def get_products():
    conn = get_db()
    products = conn.execute('''
        SELECT p.*, u.name as vendor_name, u.location as vendor_location 
        FROM products p 
        JOIN users u ON p.vendor_id = u.id
    ''').fetchall()
    return jsonify([dict(p) for p in products])

@app.route('/api/products', methods=['POST'])
def add_product():
    data = request.json
    conn = get_db()
    cur = conn.execute('''
        INSERT INTO products (name, category, price, stock, vendor_id, image, description)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (data['name'], data['category'], data['price'], data['stock'], data['vendor_id'], data.get('image', ''), data.get('description', '')))
    conn.commit()
    return jsonify({'id': cur.lastrowid}), 201

@app.route('/api/orders', methods=['POST'])
def create_order():
    data = request.json
    conn = get_db()
    # Basic order logic
    cur = conn.execute('''
        INSERT INTO orders (farmer_id, vendor_id, total, status, date)
        VALUES (?, ?, ?, ?, ?)
    ''', (data['farmer_id'], data['vendor_id'], data['total'], 'Pending', datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    return jsonify({'id': cur.lastrowid, 'message': 'Order created successfully'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
"""

seed_py = """import sqlite3
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
"""

reqs = """Flask==3.0.0
flask-cors==4.0.0
"""

create_file(os.path.join(backend_dir, 'app.py'), app_py)
create_file(os.path.join(backend_dir, 'seed.py'), seed_py)
create_file(os.path.join(backend_dir, 'requirements.txt'), reqs)

print("Backend files generated successfully.")
