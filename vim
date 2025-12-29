{% extends "base.html" %}
{% block title %}Admin Panel{% endblock %}
{% block content %}
<h2 class="mb-4"><i class="fas fa-cog"></i> Admin Panel</h2>

<!-- Add Product Form -->
<div class="card shadow-sm mb-4">
    <div class="card-header bg-primary text-white">
        <h5 class="mb-0"><i class="fas fa-plus"></i> Add New Product</h5>
    </div>
    <div class="card-body">
        <form action="{{ url_for('admin_add_product', password='admin123') }}" method="POST" class="row g-3">
            <div class="col-md-6">
                <label class="form-label">Product Name</label>
                <input type="text" class="form-control" name="name" required>
            </div>
            <div class="col-md-6">
                <label class="form-label">Category</label>
                <input type="text" class="form-control" name="category" required>
            </div>
            <div class="col-md-4">
                <label class="form-label">Price</label>
                <input type="number" step="0.01" class="form-control" name="price" required>
            </div>
            <div class="col-md-4">
                <label class="form-label">Stock</label>
                <input type="number" class="form-control" name="stock" required>
            </div>
            <div class="col-md-4">
                <label class="form-label">Image URL</label>
                <input type="url" class="form-control" name="image_url" placeholder="https://...">
            </div>
            <div class="col-12">
                <label class="form-label">Description</label>
                <textarea class="form-control" name="description" rows="2" required></textarea>
            </div>
            <div class="col-12">
                <button type="submit" class="btn btn-primary">
                    <i class="fas fa-plus"></i> Add Product
                </button>
            </div>
        </form>
    </div>
</div>

<!-- Products List -->
<div class="card shadow-sm mb-4">
    <div class="card-header bg-info text-white">
        <h5 class="mb-0"><i class="fas fa-box"></i> All Products</h5>
    </div>
    <div class="card-body">
        <div class="table-responsive">
            <table class="table table-striped">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Name</th>
                        <th>Category</th>
                        <th>Price</th>
                        <th>Stock</th>
                        <th>Action</th>
                    </tr>
                </thead>
                <tbody>
                    {% for product in products %}
                    <tr>
                        <td>{{ product.id }}</td>
                        <td>{{ product.name }}</td>
                        <td><span class="badge bg-secondary">{{ product.category }}</span></td>
                        <td>${{ "%.2f"|format(product.price) }}</td>
                        <td>{{ product.stock }}</td>
                        <td>
                            <a href="{{ url_for('admin_delete_product', id=product.id, password='admin123') }}" 
                               class="btn btn-sm btn-danger" onclick="return confirm('Delete this product?')">
                                <i class="fas fa-trash"></i>
                            </a>
                        </td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
    </div>
</div>

<!-- Orders List -->
<div class="card shadow-sm">
    <div class="card-header bg-success text-white">
        <h5 class="mb-0"><i class="fas fa-shopping-bag"></i> Recent Orders</h5>
    </div>
    <div class="card-body">
        <div class="table-responsive">
            <table class="table table-striped">
                <thead>
                    <tr>
                        <th>Order ID</th>
                        <th>Customer</th>
                        <th>Email</th>
                        <th>Phone</th>
                        <th>Total</th>
                        <th>Status</th>
                        <th>Date</th>
                    </tr>
                </thead>
                <tbody>
                    {% for order in orders %}
                    <tr>
                        <td>#{{ order.id }}</td>
                        <td>{{ order.customer_name }}</td>
                        <td>{{ order.customer_email }}</td>
                        <td>{{ order.customer_phone }}</td>
                        <td>${{ "%.2f"|format(order.total_amount) }}</td>
                        <td><span class="badge bg-success">{{ order.status }}</span></td>
                        <td>{{ order.created_at.strftime('%Y-%m-%d %H:%M') }}</td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
    </div>
</div>
{% endblock %}
