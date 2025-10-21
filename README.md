# E-Commerce Shop

A simple Django-based e-commerce application for managing products.

## Features

- **Product Management**: Create, read, update, and delete products
- **Image Upload**: Upload and display product images
- **Responsive Design**: Bootstrap-based UI that works on all devices
- **Admin Interface**: Django admin panel for product management
- **Custom Styling**: Clean, modern interface with custom CSS

## Project Structure

```
ecommerce_shop/
├── ecommerce_shop/          # Main Django project
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── shop/                    # Main app
│   ├── migrations/
│   ├── templates/shop/      # HTML templates
│   ├── css/                 # Custom CSS styles
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── images/                  # Static images folder
├── media/                   # User uploaded images
├── db.sqlite3              # SQLite database
├── manage.py               # Django management script
└── README.md
```

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### 1. Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install django
```

### 3. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 5. Run Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

## Usage

### Product Management
- **View Products**: Navigate to the home page to see all products
- **Add Product**: Click "Add New Product" to create a new product with image
- **Edit Product**: Click "Edit" on any product card
- **Delete Product**: Click "Delete" on any product card
- **View Details**: Click "View" to see full product details

### Admin Panel
Access the Django admin at `http://127.0.0.1:8000/admin/` using superuser credentials.

## Models

### Product
- `name`: Product name (CharField)
- `description`: Product description (TextField)
- `price`: Product price (DecimalField)
- `stock`: Stock quantity (IntegerField)
- `image`: Product image (ImageField, optional)
- `created_at`: Creation timestamp
- `updated_at`: Last update timestamp

## Technologies Used

- **Backend**: Django 5.2
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Database**: SQLite3
- **Image Handling**: Django's ImageField with Pillow

## File Upload

- Images are uploaded to `media/products/` directory
- Supported formats: JPG, PNG, GIF, etc.
- Images are displayed responsively in product cards and detail views

## Customization

### Styling
Modify `shop/css/styles.css` to customize the appearance.

### Templates
Edit templates in `shop/templates/shop/` to change the UI structure.

### Settings
Configure the application in `ecommerce_shop/settings.py`.

