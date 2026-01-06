# 🛒 ShopNow - E-commerce Web Application

<div align="center">

<img width="412" height="607" alt="image" src="https://github.com/user-attachments/assets/f6f7ce4e-ab0f-4d9d-a07b-3e180461fd95" />



**A modern, feature-rich e-commerce platform built with Flask and Bootstrap 5**

[Features](#-features) • [Demo](#-demo) • [Installation](#-installation) • [Usage](#-usage) • [Screenshots](#-screenshots) • [Contributing](#-contributing)

</div>

---

## 📋 Table of Contents

- [About](#-about)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Usage](#-usage)
- [Screenshots](#-screenshots)
- [Project Structure](#-project-structure)
- [API Endpoints](#-api-endpoints)
- [Configuration](#-configuration)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 About

**ShopNow** is a full-featured e-commerce web application designed for small to medium-sized online stores. Built with Flask (Python) and Bootstrap 5, it provides a clean, responsive interface for both customers and administrators.

### Why ShopNow?

- ✅ **Easy to Deploy** - Simple setup with minimal dependencies
- ✅ **Responsive Design** - Works perfectly on desktop, tablet, and mobile
- ✅ **Admin Dashboard** - Manage products and orders with ease
- ✅ **Shopping Cart** - Full cart management with quantity updates
- ✅ **Search & Filter** - Find products quickly by name or category
- ✅ **No External Database** - Uses SQLite for easy deployment

---

## ✨ Features

### 🛍️ Customer Features
- Browse products with beautiful card layouts
- Search products by name
- Filter by categories (Electronics, Home, Fashion, etc.)
- View detailed product information
- Add to cart with quantity selection
- Update cart quantities
- Secure checkout process
- Order confirmation with order ID

### 👨‍💼 Admin Features
- Admin login with password protection
- Add new products with images
- Delete products
- View all orders with customer details
- Manage product stock
- Real-time order tracking

### 🎨 UI/UX Features
- Modern gradient navbar
- Hover effects on product cards
- Responsive grid layout
- Toast notifications for user actions
- Loading states and animations
- Mobile-friendly design

---

## 🛠️ Tech Stack

### Backend
- **Flask** - Lightweight Python web framework
- **Flask-SQLAlchemy** - ORM for database operations
- **SQLite** - Embedded database

### Frontend
- **Bootstrap 5** - Responsive CSS framework
- **Font Awesome** - Icon library
- **Jinja2** - Template engine

### Development
- **Python 3.11+**
- **Vim** - Code editor (or any editor of choice)
- **Git** - Version control

---

## 📥 Installation

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- Git

### Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/shopnow-ecommerce.git
cd shopnow-ecommerce

# 2. Install dependencies
pip install Flask Flask-SQLAlchemy --break-system-packages

# 3. Run the application
python3 app.py
```

### Alternative Installation (with virtual environment)

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/shopnow-ecommerce.git
cd shopnow-ecommerce

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the application
python app.py
```

---

## 🚀 Usage

### Starting the Server

```bash
python3 app.py
```

The application will start on `http://localhost:5000`

### Accessing the Application

- **Homepage**: http://localhost:5000
- **Admin Panel**: http://localhost:5000/admin
  - Default password: `admin123`

### Sample Data

The application comes with 6 sample products:
- Laptop Gaming
- Wireless Mouse
- Coffee Maker
- T-shirt Casual
- Desk Lamp
- Bluetooth Speaker

---

## 📸 Screenshots

### Homepage
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/a1718d1d-9680-4e0e-94b9-578deb8474ee" />


*Browse all products with category filters and search*

### Product Detail
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/f7a92e97-3c23-49b1-a7a7-9842fa53935b" />


*View detailed product information and add to cart*

### Shopping Cart
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/2c97b01b-4b14-4374-b493-89c7e6194355" />


*Manage cart items and proceed to checkout*

### Admin Dashboard
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/74fc9427-e02d-4dd4-b4df-1572fb56bf2b" />


*Manage products and view orders*

---

## 📁 Project Structure

```
shopnow-ecommerce/
├── app.py                  # Main application file
├── models.py               # Database models
├── database.py             # Database configuration
├── utils.py                # Utility functions
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── SETUP_GUIDE.md         # Detailed setup guide
├── VIM_CHEATSHEET.md      # Vim editor reference
├── setup.sh               # Quick setup script
├── instance/              # Database storage
│   └── products.db        # SQLite database
├── templates/             # HTML templates
│   ├── base.html          # Base template
│   ├── index.html         # Homepage
│   ├── product_detail.html
│   ├── cart.html
│   ├── checkout.html
│   ├── order_success.html
│   ├── admin.html
│   └── admin_login.html
├── data/                  # Sample data
│   └── sample_data.json
└── tests/                 # Unit tests
    └── test_app.py
```

---

## 🔌 API Endpoints

### Public Routes

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Homepage with all products |
| GET | `/product/<id>` | Product detail page |
| GET | `/category/<category>` | Filter by category |
| GET | `/search?q=<query>` | Search products |
| GET | `/cart` | View shopping cart |
| POST | `/add_to_cart/<id>` | Add product to cart |
| POST | `/update_cart/<id>` | Update cart quantity |
| GET | `/remove_from_cart/<id>` | Remove item from cart |
| GET/POST | `/checkout` | Checkout process |
| GET | `/order_success/<id>` | Order confirmation |

### Admin Routes

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/admin?password=admin123` | Admin dashboard |
| POST | `/admin/product/add` | Add new product |
| GET | `/admin/product/delete/<id>` | Delete product |

---

## ⚙️ Configuration

### Database Configuration

Edit `app.py` to change database location:

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/products.db'
```

### Admin Password

Change the default admin password in `app.py`:

```python
if password != 'your_new_password':
    return render_template('admin_login.html')
```

### Secret Key

For production, change the secret key:

```python
app.config['SECRET_KEY'] = 'your-secret-key-here'
```

### Server Configuration

Run on different host/port:

```python
app.run(debug=True, host='0.0.0.0', port=8000)
```

---

## 🧪 Testing

Run the test suite:

```bash
python -m pytest tests/
```

Run specific test:

```bash
python tests/test_app.py
```

---

## 📦 Dependencies

```
Flask==3.0.0
Flask-SQLAlchemy==3.1.1
```

For development:

```bash
pip install -r requirements.txt
```

---

## 🌐 Deployment

### Local Network Access

The app runs on `0.0.0.0` by default, making it accessible from other devices on your network:

```
http://YOUR_IP_ADDRESS:5000
```

Find your IP:
```bash
ip addr show  # Linux
ipconfig      # Windows
```

### Production Deployment

For production deployment, consider:

1. **Use Gunicorn** (production WSGI server)
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```

2. **Use Nginx** as reverse proxy

3. **Switch to PostgreSQL** for better performance

4. **Enable HTTPS** with SSL certificate

5. **Set `debug=False`** in production

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Setup

```bash
# Clone your fork
git clone https://github.com/yourusername/shopnow-ecommerce.git

# Create a branch
git checkout -b feature/new-feature

# Make changes and test
python3 app.py

# Commit and push
git add .
git commit -m "Add new feature"
git push origin feature/new-feature
```

---

## 🐛 Known Issues

- Admin password is hardcoded (will be improved)
- No email notification for orders
- No payment gateway integration
- Limited product image management

See [Issues](https://github.com/yourusername/shopnow-ecommerce/issues) for more.

---

## 🗺️ Roadmap

- [ ] User authentication and registration
- [ ] Email notifications
- [ ] Payment gateway integration (Stripe, PayPal)
- [ ] Product reviews and ratings
- [ ] Wishlist functionality
- [ ] Order tracking
- [ ] Multi-language support
- [ ] Product image upload
- [ ] Advanced search filters
- [ ] Sales analytics dashboard

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 ShopNow E-commerce

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software...
```

---

## 👨‍💻 Author

**Iqbal**
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com

---

## 🙏 Acknowledgments

- Flask documentation and community
- Bootstrap team for the amazing CSS framework
- Font Awesome for the icon library
- Unsplash for product images
- All contributors and users of this project

---

## 📞 Support

If you have any questions or need help:

- Open an issue on GitHub
- Email: support@shopnow.com
- Discord: [Join our server](https://discord.gg/shopnow)

---

## 🌟 Show Your Support

Give a ⭐️ if this project helped you!
Thank You
---

<div align="center">

**Made with ❤️ using Flask and Bootstrap**

[⬆ Back to Top](#-shopnow---e-commerce-web-application)

</div>

MIT License

Copyright (c) 2025 ShopNow E-commerce

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
