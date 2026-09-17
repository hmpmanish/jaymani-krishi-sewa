from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'jaymani_secret_key' # Security ke liye

# Database Configuration (SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# --- DATABASE MODELS ---

class Farmer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    identifier = db.Column(db.String(100), unique=True, nullable=False) # Email ya Mobile
    password = db.Column(db.String(200), nullable=False)
    orders = db.relationship('Order', backref='farmer', lazy=True)
    ledgers = db.relationship('BahiKhata', backref='farmer', lazy=True)

class Vendor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shop_name = db.Column(db.String(100), nullable=False)
    identifier = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    products = db.relationship('Product', backref='vendor', lazy=True)
    orders = db.relationship('Order', backref='vendor', lazy=True)
    ledgers = db.relationship('BahiKhata', backref='vendor', lazy=True)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=0)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.id'), nullable=False)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    farmer_id = db.Column(db.Integer, db.ForeignKey('farmer.id'), nullable=False)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    order_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='Pending') # Pending, Completed, Cancelled

class BahiKhata(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    farmer_id = db.Column(db.Integer, db.ForeignKey('farmer.id'), nullable=False)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    transaction_type = db.Column(db.String(20), nullable=False) # 'Credit' (Udhaar) or 'Debit' (Payment)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    description = db.Column(db.String(200), nullable=True)

# Database create karne ke liye function
with app.app_context():
    db.create_all()

# --- ROUTES ---

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login_page():
    return render_template('Login.html')

@app.route('/signup')
def signup_page():
    return render_template('Signup.html')

@app.route('/auth', methods=['POST'])
def auth():
    identifier = request.form.get('identifier')
    password = request.form.get('password')
    action = request.form.get('action') # 'login' ya 'signup'
    role = request.form.get('role', 'farmer') # 'farmer' or 'vendor'

    if action == 'signup':
        hashed_pw = generate_password_hash(password, method='sha256')
        if role == 'farmer':
            existing = Farmer.query.filter_by(identifier=identifier).first()
            if existing: return "User exists!"
            new_user = Farmer(identifier=identifier, password=hashed_pw)
        else:
            existing = Vendor.query.filter_by(identifier=identifier).first()
            if existing: return "Vendor exists!"
            shop_name = request.form.get('shop_name', 'My Shop')
            new_user = Vendor(identifier=identifier, password=hashed_pw, shop_name=shop_name)
        
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login_page'))

    elif action == 'login':
        if role == 'farmer':
            user = Farmer.query.filter_by(identifier=identifier).first()
            dashboard = 'marketplace'
        else:
            user = Vendor.query.filter_by(identifier=identifier).first()
            dashboard = 'vendor_dashboard'

        if user and check_password_hash(user.password, password):
            session['user'] = identifier
            session['role'] = role
            session['user_id'] = user.id
            return redirect(url_for(dashboard))
        else:
            return "Invalid Credentials. Try again."

@app.route('/marketplace')
def marketplace():
    if 'user' not in session or session.get('role') != 'farmer':
        return redirect(url_for('login_page'))
    products = Product.query.all()
    return render_template('Marketplace.html', products=products)

@app.route('/vendor/dashboard')
def vendor_dashboard():
    if 'user' not in session or session.get('role') != 'vendor':
        return redirect(url_for('login_page'))
    products = Product.query.filter_by(vendor_id=session['user_id']).all()
    return render_template('Vendor-Dashboard.html', products=products)

@app.route('/farmer/bahi-khata')
def farmer_bahi_khata():
    if 'user' not in session or session.get('role') != 'farmer':
        return redirect(url_for('login_page'))
    ledgers = BahiKhata.query.filter_by(farmer_id=session['user_id']).all()
    return render_template('Farmer-BahiKhata.html', ledgers=ledgers)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
