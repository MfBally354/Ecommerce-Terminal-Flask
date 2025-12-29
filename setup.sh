#!/bin/bash

# 🚀 E-commerce Flask - Quick Setup Script
# Jalankan: bash setup.sh

echo "🛒 Setting up E-commerce Flask Application..."
echo "=============================================="

# Check if Python installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 not found! Installing..."
    sudo apt update
    sudo apt install python3 python3-pip python3-venv -y
fi

# Create project structure
echo "📁 Creating project structure..."
mkdir -p templates data

# Create virtual environment
echo "🐍 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "✅ Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📦 Installing Flask dependencies..."
pip install Flask Flask-SQLAlchemy

# Check if app.py exists
if [ ! -f "app.py" ]; then
    echo "⚠️  app.py not found!"
    echo "📝 Please create app.py manually with vim:"
    echo "   vim app.py"
    echo ""
    echo "Then run: python app.py"
    exit 1
fi

# Check templates
echo "🔍 Checking templates..."
required_templates=("base.html" "index.html" "cart.html" "checkout.html" "product_detail.html" "order_success.html" "admin.html" "admin_login.html")
missing_templates=()

for template in "${required_templates[@]}"; do
    if [ ! -f "templates/$template" ]; then
        missing_templates+=("$template")
    fi
done

if [ ${#missing_templates[@]} -ne 0 ]; then
    echo "⚠️  Missing templates:"
    for template in "${missing_templates[@]}"; do
        echo "   - $template"
    done
    echo ""
    echo "📝 Create missing templates with vim:"
    echo "   vim templates/<template_name>"
    echo ""
fi

# Display status
echo ""
echo "=============================================="
echo "✅ Setup completed!"
echo "=============================================="
echo ""
echo "📋 Next steps:"
echo "1. Make sure all files are created:"
echo "   - app.py"
echo "   - templates/*.html (8 files)"
echo ""
echo "2. Run the application:"
echo "   source venv/bin/activate"
echo "   python app.py"
echo ""
echo "3. Open browser:"
echo "   http://localhost:5000"
echo ""
echo "4. Admin panel:"
echo "   http://localhost:5000/admin"
echo "   Password: admin123"
echo ""
echo "=============================================="
echo "📚 Documentation: See SETUP_GUIDE.md"
echo "=============================================="
