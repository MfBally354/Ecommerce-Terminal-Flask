#!/usr/bin/env python3
"""
🛒 E-commerce Web Application
Run with: python app.py
"""

import os
from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import uuid

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ecommerce-secret-key-change-this'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Create data directory
os.makedirs('data', exist_ok=True)

# Models
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=0)
    category = db.Column(db.String(50))
    image_url = db.Column(db.String(200), default='https://via.placeholder.com/300x200')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'stock': self.stock,
            'category': self.category,
            'image_url': self.image_url
        }

class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, default=1)
    session_id = db.Column(db.String(100))
    product = db.relationship('Product')

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100))
    customer_email = db.Column(db.String(100))
    customer_phone = db.Column(db.String(20))
    total_amount = db.Column(db.Float)
    status = db.Column(db.String(20), default='pending')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Initialize session ID
@app.before_request
def before_request():
    if 'session_id' not in session:
        session['session_id'] = str(uuid.uuid4())

# Template context processor
@app.context_processor
def inject_cart_count():
    def cart_count():
        if 'session_id' in session:
            return CartItem.query.filter_by(session_id=session['session_id']).count()
        return 0
    return dict(cart_count=cart_count)

# Routes
@app.route('/')
def index():
    products = Product.query.all()
    categories = db.session.query(Product.category).distinct().all()
    return render_template('index.html', products=products, categories=categories)

@app.route('/product/<int:id>')
def product_detail(id):
    product = Product.query.get_or_404(id)
    return render_template('product_detail.html', product=product)

@app.route('/category/<category>')
def category_products(category):
    products = Product.query.filter_by(category=category).all()
    categories = db.session.query(Product.category).distinct().all()
    return render_template('index.html', products=products, categories=categories, selected_category=category)

@app.route('/search')
def search():
    query = request.args.get('q', '')
    products = Product.query.filter(Product.name.ilike(f'%{query}%')).all()
    categories = db.session.query(Product.category).distinct().all()
    return render_template('index.html', products=products, categories=categories, search_query=query)

@app.route('/cart')
def cart():
    cart_items = CartItem.query.filter_by(session_id=session['session_id']).all()
    total = sum(item.product.price * item.quantity for item in cart_items)
    return render_template('cart.html', cart_items=cart_items, total=total)

@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    product = Product.query.get_or_404(product_id)
    quantity = int(request.form.get('quantity', 1))
    
    if product.stock < quantity:
        flash('Not enough stock available!', 'error')
        return redirect(url_for('product_detail', id=product_id))
    
    cart_item = CartItem.query.filter_by(
        product_id=product_id,
        session_id=session['session_id']
    ).first()
    
    if cart_item:
        cart_item.quantity += quantity
    else:
        cart_item = CartItem(
            product_id=product_id,
            quantity=quantity,
            session_id=session['session_id']
        )
        db.session.add(cart_item)
    
    db.session.commit()
    flash(f'{product.name} added to cart!', 'success')
    return redirect(url_for('cart'))

@app.route('/update_cart/<int:item_id>', methods=['POST'])
def update_cart(item_id):
    cart_item = CartItem.query.get_or_404(item_id)
    
    if cart_item.session_id != session['session_id']:
        flash('Invalid cart item!', 'error')
        return redirect(url_for('cart'))
    
    quantity = int(request.form.get('quantity', 1))
    
    if quantity <= 0:
        db.session.delete(cart_item)
    else:
        if cart_item.product.stock < quantity:
            flash('Not enough stock!', 'error')
            return redirect(url_for('cart'))
        cart_item.quantity = quantity
    
    db.session.commit()
    flash('Cart updated!', 'success')
    return redirect(url_for('cart'))

@app.route('/remove_from_cart/<int:item_id>')
def remove_from_cart(item_id):
    cart_item = CartItem.query.get_or_404(item_id)
    
    if cart_item.session_id == session['session_id']:
        db.session.delete(cart_item)
        db.session.commit()
        flash('Item removed from cart!', 'success')
    
    return redirect(url_for('cart'))

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    cart_items = CartItem.query.filter_by(session_id=session['session_id']).all()
    
    if not cart_items:
        flash('Your cart is empty!', 'error')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        
        total = sum(item.product.price * item.quantity for item in cart_items)
        
        # Check stock
        for item in cart_items:
            if item.product.stock < item.quantity:
                flash(f'Not enough stock for {item.product.name}', 'error')
                return redirect(url_for('cart'))
        
        # Create order
        order = Order(
            customer_name=name,
            customer_email=email,
            customer_phone=phone,
            total_amount=total,
            status='completed'
        )
        db.session.add(order)
        
        # Update stock
        for item in cart_items:
            item.product.stock -= item.quantity
        
        # Clear cart
        CartItem.query.filter_by(session_id=session['session_id']).delete()
        
        db.session.commit()
        
        flash(f'Order placed successfully! Order ID: {order.id}', 'success')
        return redirect(url_for('order_success', order_id=order.id))
    
    total = sum(item.product.price * item.quantity for item in cart_items)
    return render_template('checkout.html', cart_items=cart_items, total=total)

@app.route('/order_success/<int:order_id>')
def order_success(order_id):
    order = Order.query.get_or_404(order_id)
    return render_template('order_success.html', order=order)

@app.route('/admin')
def admin():
    password = request.args.get('password')
    if password != 'admin123':
        return render_template('admin_login.html')
    
    products = Product.query.all()
    orders = Order.query.order_by(Order.created_at.desc()).all()
    return render_template('admin.html', products=products, orders=orders)

@app.route('/admin/product/add', methods=['POST'])
def admin_add_product():
    if request.args.get('password') != 'admin123':
        return redirect(url_for('admin'))
    
    product = Product(
        name=request.form.get('name'),
        description=request.form.get('description'),
        price=float(request.form.get('price')),
        stock=int(request.form.get('stock')),
        category=request.form.get('category'),
        image_url=request.form.get('image_url', 'https://via.placeholder.com/300x200')
    )
    db.session.add(product)
    db.session.commit()
    
    flash('Product added successfully!', 'success')
    return redirect(url_for('admin', password='admin123'))

@app.route('/admin/product/delete/<int:id>')
def admin_delete_product(id):
    if request.args.get('password') != 'admin123':
        return redirect(url_for('admin'))
    
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    
    flash('Product deleted!', 'success')
    return redirect(url_for('admin', password='admin123'))

# Initialize database
def init_db():
    with app.app_context():
        db.create_all()
        
        if Product.query.count() == 0:
            sample_products = [
                Product(name='Laptop Gaming', description='High-performance gaming laptop with RTX 4070', 
                       price=1299.99, stock=10, category='Electronics', 
                       image_url='https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=300'),
                Product(name='Wireless Mouse', description='Ergonomic wireless mouse with RGB lighting', 
                       price=29.99, stock=50, category='Electronics',
                       image_url='https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=300'),
                Product(name='Coffee Maker', description='Automatic coffee machine with timer', 
                       price=89.99, stock=15, category='Home',
                       image_url='https://images.unsplash.com/photo-1517668808822-9ebb02f2a0e6?w=300'),
                Product(name='T-shirt Casual', description='100% cotton t-shirt, various colors', 
                       price=19.99, stock=100, category='Fashion',
                       image_url='https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=300'),
                Product(name='Desk Lamp', description='LED desk lamp with adjustable brightness', 
                       price=34.99, stock=25, category='Home',
                       image_url='https://images.unsplash.com/photo-1507473885765-e6ed057f782c?w=300'),
                Product(name='Bluetooth Speaker', description='Portable waterproof speaker with 20h battery', 
                       price=59.99, stock=30, category='Electronics',
                       image_url='https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=300'),
            ]
            for product in sample_products:
                db.session.add(product)
            db.session.commit()
            print("✅ Sample products added!")

if __name__ == '__main__':
    init_db()
    print("🚀 Starting E-commerce Web App...")
    print("📍 Open: http://localhost:5000")
    print("🔐 Admin: http://localhost:5000/admin (password: admin123)")
    app.run(debug=True, host='0.0.0.0', port=5000)
