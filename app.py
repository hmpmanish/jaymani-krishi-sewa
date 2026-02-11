from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'jaymani_secret_key' # Security ke liye

# Database Configuration (SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# Farmer Model (Database Table)
class Farmer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    identifier = db.Column(db.String(100), unique=True, nullable=False) # Email ya Mobile
    password = db.Column(db.String(200), nullable=False)

# Database create karne ke liye function
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/auth', methods=['POST'])
def auth():
    # Frontend se data lena
    identifier = request.form.get('identifier')
    password = request.form.get('password')
    action = request.form.get('action') # 'login' ya 'signup'

    if action == 'signup':
        # Check if user exists
        existing_user = Farmer.query.filter_by(identifier=identifier).first()
        if existing_user:
            return "User already exists! Please login."
        
        # New Farmer Create karein
        hashed_pw = generate_password_hash(password, method='sha256')
        new_farmer = Farmer(identifier=identifier, password=hashed_pw)
        db.session.add(new_farmer)
        db.session.commit()
        return "Account Created Successfully! Now Login."

    elif action == 'login':
        farmer = Farmer.query.filter_by(identifier=identifier).first()
        if farmer and check_password_hash(farmer.password, password):
            session['user'] = identifier
            return f"Welcome {identifier}! Login Successful."
        else:
            return "Invalid Credentials. Try again."

if __name__ == '__main__':
    app.run(debug=True)
