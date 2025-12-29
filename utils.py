import os
import json
from rich.console import Console
from rich.table import Table
from rich import print as rprint
from tabulate import tabulate

console = Console()

def clear_screen():
    """Clear terminal screen"""
    os.system('clear' if os.name == 'posix' else 'cls')

def display_title(title):
    """Display beautiful title"""
    clear_screen()
    console.rule(f"[bold cyan]🛒 {title}[/bold cyan]")
    print()

def display_products_table(products):
    """Display products in table format"""
    if not products:
        print("📭 No products available")
        return
    
    table_data = []
    for product in products:
        table_data.append([
            product.id,
            product.name[:30] + "..." if len(product.name) > 30 else product.name,
            product.category,
            f"${product.price:.2f}",
            f"{product.stock} pcs",
            "✅ In Stock" if product.stock > 0 else "❌ Out of Stock"
        ])
    
    headers = ["ID", "Name", "Category", "Price", "Stock", "Status"]
    print(tabulate(table_data, headers=headers, tablefmt="grid"))
    print()

def display_cart_table(cart_items):
    """Display cart items in table format"""
    if not cart_items:
        print("🛒 Your cart is empty")
        return
    
    table = Table(title="🛍️  Your Shopping Cart")
    table.add_column("Product", style="cyan")
    table.add_column("Price", style="green")
    table.add_column("Qty", style="yellow")
    table.add_column("Subtotal", style="bold green")
    
    total = 0
    for item in cart_items:
        subtotal = item.product.price * item.quantity
        total += subtotal
        table.add_row(
            item.product.name,
            f"${item.product.price:.2f}",
            str(item.quantity),
            f"${subtotal:.2f}"
        )
    
    console.print(table)
    console.print(f"\n[bold]Total: [green]${total:.2f}[/green][/bold]")
    return total

def load_sample_data():
    """Load sample products"""
    sample_products = [
        {
            'name': 'Laptop Gaming',
            'description': 'High-performance gaming laptop',
            'price': 1299.99,
            'stock': 10,
            'category': 'Electronics'
        },
        {
            'name': 'Wireless Mouse',
            'description': 'Ergonomic wireless mouse',
            'price': 29.99,
            'stock': 50,
            'category': 'Electronics'
        },
        {
            'name': 'Coffee Maker',
            'description': 'Automatic coffee machine',
            'price': 89.99,
            'stock': 15,
            'category': 'Home'
        },
        {
            'name': 'T-shirt Casual',
            'description': '100% cotton t-shirt',
            'price': 19.99,
            'stock': 100,
            'category': 'Fashion'
        },
        {
            'name': 'Desk Lamp',
            'description': 'LED desk lamp with dimmer',
            'price': 34.99,
            'stock': 25,
            'category': 'Home'
        },
        {
            'name': 'Bluetooth Speaker',
            'description': 'Portable waterproof speaker',
            'price': 59.99,
            'stock': 30,
            'category': 'Electronics'
        }
    ]
    return sample_products
