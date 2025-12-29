# 🚀 Panduan Setup E-commerce Flask di Linux

## 📋 Persiapan

### 1. Install Requirements
```bash
# Update package manager
sudo apt update
sudo apt install python3 python3-pip python3-venv vim -y
```

### 2. Buat Folder Proyek
```bash
# Buat dan masuk ke folder proyek
mkdir ecommerce-web
cd ecommerce-web

# Buat virtual environment
python3 -m venv venv

# Aktifkan virtual environment
source venv/bin/activate

# Install Flask
pip install Flask Flask-SQLAlchemy
```

### 3. Buat Struktur Folder
```bash
# Buat folder templates dan data
mkdir templates
mkdir data
```

## 📝 Cara Pakai Vim (Editor Terminal)

### Perintah Dasar Vim:
- `i` = Masuk mode INSERT (bisa mengetik)
- `Esc` = Keluar dari mode INSERT
- `:w` = Save file
- `:q` = Quit vim
- `:wq` = Save & quit
- `:q!` = Quit tanpa save
- `dd` = Delete 1 baris (di mode normal)
- `yy` = Copy 1 baris
- `p` = Paste

### Tips Copy-Paste di Vim:
1. Buka vim: `vim namafile.py`
2. Tekan `i` untuk masuk mode INSERT
3. Klik kanan → Paste (atau Ctrl+Shift+V)
4. Tekan `Esc`
5. Ketik `:wq` lalu Enter

## 📦 Buat File-file Proyek

### File 1: app.py
```bash
vim app.py
```
Tekan `i`, paste kode app.py dari artifact pertama, `Esc`, ketik `:wq`, Enter.

### File 2: templates/base.html
```bash
vim templates/base.html
```
Paste kode base.html, save dengan `:wq`

### File 3: templates/index.html
```bash
vim templates/index.html
```
Paste kode index.html, save dengan `:wq`

### File 4: templates/product_detail.html
```bash
vim templates/product_detail.html
```
Paste kode product_detail.html, save dengan `:wq`

### File 5: templates/cart.html
```bash
vim templates/cart.html
```
Paste kode cart.html, save dengan `:wq`

### File 6: templates/checkout.html
```bash
vim templates/checkout.html
```
Paste kode checkout.html, save dengan `:wq`

### File 7: templates/order_success.html
```bash
vim templates/order_success.html
```
Paste kode order_success.html, save dengan `:wq`

### File 8: templates/admin_login.html
```bash
vim templates/admin_login.html
```
Paste kode admin_login.html, save dengan `:wq`

### File 9: templates/admin.html
```bash
vim templates/admin.html
```
Paste kode admin.html (dari artifact admin_templates), save dengan `:wq`

## 🚀 Menjalankan Aplikasi

### Cara 1: Jalankan di Localhost
```bash
# Pastikan virtual environment aktif
source venv/bin/activate

# Jalankan aplikasi
python app.py
```

Buka browser: `http://localhost:5000`

### Cara 2: Jalankan di Background (tmux/screen)
```bash
# Install tmux
sudo apt install tmux -y

# Buat session baru
tmux new -s ecommerce

# Jalankan aplikasi
python app.py

# Detach dari session: Ctrl+B lalu D
# Attach kembali: tmux attach -t ecommerce
```

### Cara 3: Akses dari Network Luar
```bash
# Aplikasi sudah set host='0.0.0.0'
# Cek IP server kamu:
ip addr show

# Akses dari komputer lain:
# http://IP_SERVER:5000
```

## 🔧 Konfigurasi Firewall (Jika Perlu)

```bash
# Ubuntu/Debian
sudo ufw allow 5000/tcp
sudo ufw reload

# CentOS/RHEL
sudo firewall-cmd --add-port=5000/tcp --permanent
sudo firewall-cmd --reload
```

## 📱 Fitur-fitur Aplikasi

1. **Homepage** - `http://localhost:5000`
   - Browse semua produk
   - Filter by category
   - Search products

2. **Product Detail** - Klik produk untuk detail
   - Lihat info lengkap
   - Add to cart dengan quantity

3. **Shopping Cart** - `http://localhost:5000/cart`
   - Update quantity
   - Remove items
   - Proceed to checkout

4. **Checkout** - Isi data customer
   - Form pemesanan
   - Konfirmasi order

5. **Admin Panel** - `http://localhost:5000/admin`
   - Login password: `admin123`
   - Add/Delete products
   - View orders

## 🐛 Troubleshooting

### Error: Port 5000 sudah dipakai
```bash
# Cari proses yang pakai port 5000
sudo lsof -i :5000

# Kill proses
sudo kill -9 <PID>

# Atau ubah port di app.py:
# app.run(debug=True, host='0.0.0.0', port=8000)
```

### Error: Permission denied
```bash
# Pastikan file executable
chmod +x app.py

# Atau jalankan dengan python3
python3 app.py
```

### Error: Module not found
```bash
# Reinstall dependencies
pip install --upgrade Flask Flask-SQLAlchemy
```

### Database tidak terbuat
```bash
# Hapus database lama
rm -rf data/products.db

# Jalankan ulang aplikasi
python app.py
```

## 📊 Struktur Folder Final

```
ecommerce-web/
├── venv/               # Virtual environment
├── data/
│   └── products.db     # SQLite database (auto-generated)
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── product_detail.html
│   ├── cart.html
│   ├── checkout.html
│   ├── order_success.html
│   ├── admin_login.html
│   └── admin.html
└── app.py              # Main application
```

## 🎯 Next Steps

1. **Customize Design**: Edit file CSS di base.html
2. **Add Features**: Edit app.py untuk tambah fitur
3. **Deploy Production**: Gunakan Gunicorn + Nginx
4. **Database**: Ganti ke PostgreSQL untuk production

## 💡 Tips Vim Produktif

### Edit Multiple Files
```bash
# Buka beberapa file sekaligus
vim templates/*.html

# Switch antar file:
:next   # File berikutnya
:prev   # File sebelumnya
:ls     # List semua file
```

### Search & Replace di Vim
```bash
# Search: /keyword
# Replace all: :%s/old/new/g
```

### Visual Mode (Select Text)
```bash
# Tekan 'v' untuk visual mode
# Arrow keys untuk select
# 'y' untuk copy, 'd' untuk cut
# 'p' untuk paste
```

## 🔒 Keamanan Production

**PENTING**: Sebelum deploy:
1. Ubah `SECRET_KEY` di app.py
2. Ganti password admin default
3. Set `debug=False`
4. Gunakan database production (PostgreSQL)
5. Setup HTTPS dengan SSL certificate

## ✅ Checklist Setup

- [ ] Install Python & Vim
- [ ] Buat virtual environment
- [ ] Install Flask dependencies
- [ ] Buat semua file dengan Vim
- [ ] Test run aplikasi
- [ ] Akses via browser
- [ ] Test semua fitur (browse, cart, checkout, admin)
- [ ] Backup database

---

**Selamat! Aplikasi E-commerce Flask sudah siap digunakan! 🎉**
