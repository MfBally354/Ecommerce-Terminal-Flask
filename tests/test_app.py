import unittest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app, db, Product

class EcommerceTestCase(unittest.TestCase):
    """Test cases for e-commerce app"""
    
    def setUp(self):
        """Set up test database"""
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        
        with app.app_context():
            db.create_all()
    
    def tearDown(self):
        """Clean up after tests"""
        with app.app_context():
            db.session.remove()
            db.drop_all()
    
    def test_home_page(self):
        """Test if home page loads"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'E-commerce Terminal API', response.data)
    
    def test_product_model(self):
        """Test Product model creation"""
        with app.app_context():
            product = Product(
                name="Test Product",
                description="Test Description",
                price=99.99,
                stock=10,
                category="Test"
            )
            db.session.add(product)
            db.session.commit()
            
            # Retrieve product
            saved_product = Product.query.first()
            self.assertEqual(saved_product.name, "Test Product")
            self.assertEqual(saved_product.price, 99.99)

if __name__ == '__main__':
    unittest.main()
