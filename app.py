#!/usr/bin/env python3
"""
🛒 E-commerce Terminal Application
Run with: python app.py
"""

import os
import uuid
from flask import Flask, session, request, jsonify
from models import Product, CartItem, Order, db
from utils import (
    display_title, display_products_table, 
    display_cart_table, clear_screen, load_sample_data
)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ecommerce-terminal-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Create data directory if not exists
os.makedirs('data', exist_ok=True)

class ECommerceTerminal:
    """Main terminal application class"""
    
    def __init__(self):
        self.session_id = str(uuid.uuid4())
        self.running = True
        
    def init_database(self):
        """Initialize database with sample data"""
        with app.app_context():
            db.create_all()
            
            # Add sample products if empty
            if Product.query.count() == 0:
                sample_products = load_sample_data()
                for prod_data in sample_products:
                    product = Product(**prod_data)
                    db.session.add(product)
                db.session.commit()
                print("✅ Sample products added!")
    
    def main_menu(self):
        """Display main menu"""
        while self.running:
            display_title("E-Commerce Terminal")
            print("1. 📋 Browse Products")
            print("2. 🛒 View Cart")
            print("3. 🔍 Search Products")
            print("4. 📦 Manage Products (Admin)")
            print("5. 📝 Place Order")
            print("6. 📊 View Orders")
            print("7. ❌ Exit")
            print("\n" + "="*50)
            
            choice = input("\nSelect option (1-7): ").strip()
            
            if choice == '1':
                self.browse_products()
            elif choice == '2':
                self.view_cart()
            elif choice == '3':
                self.search_products()
            elif choice == '4':
                self.manage_products()
            elif choice == '5':
                self.place_order()
            elif choice == '6':
                self.view_orders()
            elif choice == '7':
                print("\n👋 Thank you for shopping with us!")
                self.running = False
            else:
                print("❌ Invalid choice. Please try again.")
                input("\nPress Enter to continue...")
    
    def browse_products(self):
        """Browse all products"""
        with app.app_context():
            products = Product.query.all()
            
            display_title("All Products")
            display_products_table(products)
            
            print("\nOptions:")
            print("1. Add to cart")
            print("2. View product details")
            print("3. Back to main menu")
            
            choice = input("\nSelect option (1-3): ").strip()
            
            if choice == '1':
                product_id = input("Enter product ID to add to cart: ").strip()
                if product_id.isdigit():
                    self.add_to_cart(int(product_id))
                else:
                    print("❌ Invalid product ID")
            elif choice == '2':
                product_id = input("Enter product ID to view details: ").strip()
                if product_id.isdigit():
                    self.view_product_details(int(product_id))
            elif choice == '3':
                return
            else:
                print("❌ Invalid choice")
            
            input("\nPress Enter to continue...")
    
    def add_to_cart(self, product_id):
        """Add product to cart"""
        with app.app_context():
            product = Product.query.get(product_id)
            
            if not product:
                print("❌ Product not found")
                return
            
            if product.stock <= 0:
                print("❌ Product out of stock")
                return
            
            quantity = input(f"Enter quantity (max {product.stock}): ").strip()
            if not quantity.isdigit() or int(quantity) <= 0:
                print("❌ Invalid quantity")
                return
            
            quantity = int(quantity)
            if quantity > product.stock:
                print(f"❌ Only {product.stock} items available")
                return
            
            # Check if product already in cart
            cart_item = CartItem.query.filter_by(
                product_id=product_id,
                session_id=self.session_id
            ).first()
            
            if cart_item:
                cart_item.quantity += quantity
            else:
                cart_item = CartItem(
                    product_id=product_id,
                    quantity=quantity,
                    session_id=self.session_id
                )
                db.session.add(cart_item)
            
            db.session.commit()
            print(f"✅ Added {quantity} x {product.name} to cart!")
    
    def view_cart(self):
        """View shopping cart"""
        with app.app_context():
            cart_items = CartItem.query.filter_by(
                session_id=self.session_id
            ).join(Product).all()
            
            display_title("Shopping Cart")
            total = display_cart_table(cart_items)
            
            if not cart_items:
                input("\nPress Enter to continue...")
                return
            
            print("\nOptions:")
            print("1. Update quantity")
            print("2. Remove item")
            print("3. Clear cart")
            print("4. Checkout")
            print("5. Back to main menu")
            
            choice = input("\nSelect option (1-5): ").strip()
            
            if choice == '1':
                item_id = input("Enter item ID to update: ").strip()
                if item_id.isdigit():
                    self.update_cart_item(int(item_id))
            elif choice == '2':
                item_id = input("Enter item ID to remove: ").strip()
                if item_id.isdigit():
                    self.remove_cart_item(int(item_id))
            elif choice == '3':
                self.clear_cart()
            elif choice == '4':
                self.checkout()
            elif choice == '5':
                return
            else:
                print("❌ Invalid choice")
            
            input("\nPress Enter to continue...")
    
    def update_cart_item(self, item_id):
        """Update cart item quantity"""
        with app.app_context():
            cart_item = CartItem.query.get(item_id)
            
            if not cart_item or cart_item.session_id != self.session_id:
                print("❌ Item not found in your cart")
                return
            
            product = Product.query.get(cart_item.product_id)
            
            new_quantity = input(f"Enter new quantity (max {product.stock}): ").strip()
            if not new_quantity.isdigit() or int(new_quantity) <= 0:
                print("❌ Invalid quantity")
                return
            
            new_quantity = int(new_quantity)
            if new_quantity > product.stock:
                print(f"❌ Only {product.stock} items available")
                return
            
            cart_item.quantity = new_quantity
            db.session.commit()
            print("✅ Cart updated!")
    
    def remove_cart_item(self, item_id):
        """Remove item from cart"""
        with app.app_context():
            cart_item = CartItem.query.get(item_id)
            
            if not cart_item or cart_item.session_id != self.session_id:
                print("❌ Item not found in your cart")
                return
            
            db.session.delete(cart_item)
            db.session.commit()
            print("✅ Item removed from cart!")
    
    def clear_cart(self):
        """Clear all items from cart"""
        with app.app_context():
            cart_items = CartItem.query.filter_by(session_id=self.session_id).all()
            
            for item in cart_items:
                db.session.delete(item)
            
            db.session.commit()
            print("✅ Cart cleared!")
    
    def checkout(self):
        """Process checkout"""
        with app.app_context():
            cart_items = CartItem.query.filter_by(
                session_id=self.session_id
            ).join(Product).all()
            
            if not cart_items:
                print("❌ Your cart is empty")
                return
            
            display_title("Checkout")
            total = display_cart_table(cart_items)
            
            print("\nPlease enter your details:")
            name = input("Full Name: ").strip()
            if not name:
                print("❌ Name is required")
                return
            
            print(f"\nTotal Amount: ${total:.2f}")
            confirm = input("\nConfirm order? (y/n): ").strip().lower()
            
            if confirm == 'y':
                # Check stock availability
                for item in cart_items:
                    if item.product.stock < item.quantity:
                        print(f"❌ Not enough stock for {item.product.name}")
                        return
                
                # Update stock and create order
                for item in cart_items:
                    item.product.stock -= item.quantity
                
                order = Order(
                    customer_name=name,
                    total_amount=total,
                    status='completed'
                )
                db.session.add(order)
                
                # Clear cart
                CartItem.query.filter_by(session_id=self.session_id).delete()
                
                db.session.commit()
                print(f"\n🎉 Order placed successfully! Order ID: {order.id}")
                print("Thank you for your purchase!")
            else:
                print("❌ Order cancelled")
    
    def search_products(self):
        """Search products by name or category"""
        display_title("Search Products")
        
        print("Search by:")
        print("1. Product name")
        print("2. Category")
        print("3. Price range")
        print("4. Back to main menu")
        
        choice = input("\nSelect option (1-4): ").strip()
        
        with app.app_context():
            if choice == '1':
                keyword = input("Enter product name: ").strip()
                products = Product.query.filter(
                    Product.name.ilike(f'%{keyword}%')
                ).all()
            elif choice == '2':
                category = input("Enter category: ").strip()
                products = Product.query.filter_by(category=category).all()
            elif choice == '3':
                min_price = input("Minimum price: ").strip()
                max_price = input("Maximum price: ").strip()
                
                try:
                    min_price = float(min_price) if min_price else 0
                    max_price = float(max_price) if max_price else float('inf')
                    
                    products = Product.query.filter(
                        Product.price.between(min_price, max_price)
                    ).all()
                except ValueError:
                    print("❌ Invalid price")
                    products = []
            elif choice == '4':
                return
            else:
                print("❌ Invalid choice")
                return
            
            display_title("Search Results")
            display_products_table(products)
            
            if products:
                print("\nOptions:")
                print("1. Add to cart")
                print("2. New search")
                print("3. Back to main menu")
                
                sub_choice = input("\nSelect option (1-3): ").strip()
                
                if sub_choice == '1':
                    product_id = input("Enter product ID to add to cart: ").strip()
                    if product_id.isdigit():
                        self.add_to_cart(int(product_id))
                elif sub_choice == '2':
                    self.search_products()
                    return
                elif sub_choice == '3':
                    return
            
            input("\nPress Enter to continue...")
    
    def view_product_details(self, product_id):
        """View detailed product information"""
        with app.app_context():
            product = Product.query.get(product_id)
            
            if not product:
                print("❌ Product not found")
                return
            
            display_title(f"Product Details - {product.name}")
            
            print(f"📦 Name: {product.name}")
            print(f"📝 Description: {product.description}")
            print(f"💰 Price: ${product.price:.2f}")
            print(f"📊 Stock: {product.stock} units")
            print(f"🏷️  Category: {product.category}")
            print(f"📅 Added: {product.created_at.strftime('%Y-%m-%d')}")
            
            print("\nOptions:")
            print("1. Add to cart")
            print("2. Back to product list")
            
            choice = input("\nSelect option (1-2): ").strip()
            
            if choice == '1':
                self.add_to_cart(product_id)
    
    def manage_products(self):
        """Admin: Manage products"""
        display_title("Product Management")
        
        print("Admin Password required (default: admin123)")
        password = input("Password: ").strip()
        
        if password != "admin123":
            print("❌ Access denied")
            input("\nPress Enter to continue...")
            return
        
        print("\nAdmin Menu:")
        print("1. Add new product")
        print("2. Update product")
        print("3. Delete product")
        print("4. View all products")
        print("5. Back to main menu")
        
        choice = input("\nSelect option (1-5): ").strip()
        
        if choice == '1':
            self.add_product()
        elif choice == '2':
            self.update_product()
        elif choice == '3':
            self.delete_product()
        elif choice == '4':
            self.browse_products()
        elif choice == '5':
            return
        else:
            print("❌ Invalid choice")
        
        input("\nPress Enter to continue...")
    
    def add_product(self):
        """Add new product"""
        display_title("Add New Product")
        
        print("Enter product details:")
        name = input("Product Name: ").strip()
        description = input("Description: ").strip()
        price = input("Price: ").strip()
        stock = input("Stock Quantity: ").strip()
        category = input("Category: ").strip()
        
        try:
            price = float(price)
            stock = int(stock)
            
            with app.app_context():
                product = Product(
                    name=name,
                    description=description,
                    price=price,
                    stock=stock,
                    category=category
                )
                db.session.add(product)
                db.session.commit()
            
            print("✅ Product added successfully!")
        except ValueError:
            print("❌ Invalid price or stock value")
    
    def update_product(self):
        """Update existing product"""
        with app.app_context():
            products = Product.query.all()
            
            display_title("Update Product")
            display_products_table(products)
            
            if not products:
                return
            
            product_id = input("\nEnter product ID to update: ").strip()
            if not product_id.isdigit():
                print("❌ Invalid product ID")
                return
            
            product = Product.query.get(int(product_id))
            if not product:
                print("❌ Product not found")
                return
            
            print(f"\nUpdating: {product.name}")
            print("Leave blank to keep current value")
            
            name = input(f"New name [{product.name}]: ").strip()
            description = input(f"New description [{product.description}]: ").strip()
            price = input(f"New price [${product.price}]: ").strip()
            stock = input(f"New stock [{product.stock}]: ").strip()
            category = input(f"New category [{product.category}]: ").strip()
            
            if name:
                product.name = name
            if description:
                product.description = description
            if price:
                try:
                    product.price = float(price)
                except ValueError:
                    print("❌ Invalid price format")
            if stock:
                try:
                    product.stock = int(stock)
                except ValueError:
                    print("❌ Invalid stock format")
            if category:
                product.category = category
            
            db.session.commit()
            print("✅ Product updated successfully!")
    
    def delete_product(self):
        """Delete product"""
        with app.app_context():
            products = Product.query.all()
            
            display_title("Delete Product")
            display_products_table(products)
            
            if not products:
                return
            
            product_id = input("\nEnter product ID to delete: ").strip()
            if not product_id.isdigit():
                print("❌ Invalid product ID")
                return
            
            product = Product.query.get(int(product_id))
            if not product:
                print("❌ Product not found")
                return
            
            confirm = input(f"Are you sure you want to delete '{product.name}'? (y/n): ").strip().lower()
            
            if confirm == 'y':
                db.session.delete(product)
                db.session.commit()
                print("✅ Product deleted successfully!")
            else:
                print("❌ Deletion cancelled")
    
    def view_orders(self):
        """View all orders"""
        with app.app_context():
            orders = Order.query.order_by(Order.created_at.desc()).all()
            
            display_title("All Orders")
            
            if not orders:
                print("📭 No orders found")
                input("\nPress Enter to continue...")
                return
            
            from tabulate import tabulate
            
            table_data = []
            for order in orders:
                table_data.append([
                    order.id,
                    order.customer_name,
                    f"${order.total_amount:.2f}",
                    order.status,
                    order.created_at.strftime('%Y-%m-%d %H:%M')
                ])
            
            headers = ["Order ID", "Customer", "Total", "Status", "Date"]
            print(tabulate(table_data, headers=headers, tablefmt="grid"))
            
            input("\nPress Enter to continue...")
    
    def place_order(self):
        """Place order directly"""
        self.view_cart()
        if CartItem.query.filter_by(session_id=self.session_id).count() > 0:
            self.checkout()
    
    def run(self):
        """Run the terminal application"""
        clear_screen()
        print("🛒 Initializing E-Commerce Terminal...")
        self.init_database()
        print("✅ System ready!")
        input("\nPress Enter to start shopping...")
        self.main_menu()


def run_flask_api():
    """Run Flask API server (optional)"""
    @app.route('/')
    def home():
        return jsonify({
            'message': 'E-commerce Terminal API',
            'status': 'running'
        })
    
    @app.route('/api/products', methods=['GET'])
    def get_products():
        products = Product.query.all()
        return jsonify([p.to_dict() for p in products])
    
    print("\n🌐 Starting Flask API server on http://localhost:5000")
    print("Press Ctrl+C to stop the server")
    app.run(debug=False, port=5000)


if __name__ == '__main__':
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == '--api':
        # Run as API server
        with app.app_context():
            db.create_all()
        run_flask_api()
    else:
        # Run terminal interface
        terminal = ECommerceTerminal()
        terminal.run()
