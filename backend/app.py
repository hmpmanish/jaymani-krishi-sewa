from flask import Flask, request, jsonify
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
