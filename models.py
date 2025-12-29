from database import db
from datetime import datetime

class Product(db.Model):
    """Product model"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=0)
    category = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Product {self.name}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'stock': self.stock,
            'category': self.category
        }

class CartItem(db.Model):
    """Shopping cart item model"""
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, default=1)
    session_id = db.Column(db.String(100))
    
    product = db.relationship('Product')
    
    def __repr__(self):
        return f'<CartItem {self.product.name} x{self.quantity}>'

class Order(db.Model):
    """Order model"""
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100))
    total_amount = db.Column(db.Float)
    status = db.Column(db.String(20), default='pending')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Order {self.id} - {self.customer_name}>'
