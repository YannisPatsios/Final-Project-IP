# SDR World

A modern Django e-commerce platform for Software Defined Radios (SDRs) and accessories.

---

## 🌟 Features
- Product catalogue with category & subcategory browsing
- Search and advanced AJAX filtering (brand, price)
- User registration, login, logout, profile edit
- Personalized dashboard (recently viewed, reviews, cart summary)
- AJAX-powered star ratings and reviews
- Custom admin panel (no Django default admin)
- Shopping cart simulation (add/remove/update/checkout, no payments)
- Recommender system for similar items
- Media uploads (product images, avatars)
- **All CSS and JS assets organized in the `static/` folder**
- Beautiful Bootstrap 5 styling, jQuery, AJAX

## 🚀 Tech Stack
- **Backend:** Django 4.x, Python 3.11+
- **Frontend:** Bootstrap 5, HTML5, CSS3, jQuery
- **Database:** SQLite (development)
- **Other:** crispy-forms, crispy-bootstrap5

## 🗂️ Project Structure
```text
Final-Project-IP/
├── accounts/           # User management app
├── adminpanel/         # Custom admin dashboard & CRUD
├── cart/               # Shopping cart logic
├── dashboard/          # User dashboard
├── media/              # Uploaded media (avatars, product images)
│   ├── avatars/
│   └── products/
├── products/           # Product catalogue app
├── reviews/            # Product reviews & ratings
├── sdr_world/          # Django project settings
├── static/             # Static assets (CSS, JS)
│   ├── css/
│   │   └── main.css
│   └── js/
│       └── main.js
├── templates/          # HTML templates (per app)
│   ├── base.html
│   ├── accounts/
│   ├── adminpanel/
│   ├── cart/
│   ├── dashboard/
│   ├── products/
│   └── reviews/
├── db.sqlite3          # SQLite database (dev)
├── manage.py           # Django management script
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

## ⚡ Quickstart
1. **Clone the repo:**
   ```bash
   git clone <https://github.com/YannisPatsios/Final-Project-IP>
   cd Final-Project-IP
   ```
2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run migrations:**
   ```bash
   python manage.py migrate
   ```
5. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```
6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```
7. **Access the app:**
   - Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser, unless it is deployed online.

## 🛠️ Deployment
- Ready for deployment on Render, Railway, or similar platforms.
- Configure static/media settings for production as needed.

---
**Note:** This project does not use Django's default admin. All admin features are custom-built in the `adminpanel` app.

---

## 👏 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.


