# SDR World

A Django 4.x e-commerce platform for Software Defined Radios (SDRs) and accessories.

## Features
- Product catalogue with category & subcategory browsing
- Search and advanced AJAX filtering (brand, price)
- User registration, login, logout, profile edit
- Personalized dashboard (recently viewed, reviews, cart summary)
- AJAX-powered star ratings and reviews
- Custom admin panel (no Django default admin)
- Shopping cart simulation (add/remove/update/checkout, no payments)
- Recommender system for similar items
- Media uploads (product images, avatars)
- Bootstrap 5 styling, jQuery, AJAX

## Tech Stack
- Django 4.x, Python 3.11+
- SQLite (development)
- Bootstrap 5, HTML5, CSS3, jQuery
- crispy-forms, crispy-bootstrap5

## Folder Structure
- `sdr_world/` – Django project settings
- `products/`, `accounts/`, `dashboard/`, `adminpanel/`, `cart/`, `reviews/` – Django apps
- `templates/` – All HTML templates (per app)
- `static/` – Static files (css, js, img)
- `media/` – Uploaded media (product images, avatars)

## Setup
1. Clone the repo
2. Create and activate a virtual environment
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```bash
   python manage.py migrate
   ```
5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
6. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Deployment
Ready for deployment on Render, Railway, or similar platforms.

---
**Note:** This project does not use Django's default admin. All admin features are custom-built in the `adminpanel` app.
