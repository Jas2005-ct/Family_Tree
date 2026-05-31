# 🌳 Family Tree

An interactive family tree web application built with **Django 5**, **Bootstrap 5**, **Alpine.js**, and **HTMX**.

## ✨ Features

- 🌳 Interactive SVG node-connection family tree
- 👤 Click any node to view person details
- 🔐 Admin panel to add/edit/delete family members
- ⚡ HTMX-powered forms (no page reloads)
- 🏔️ Alpine.js for smooth UI interactions
- 📱 Fully responsive (Bootstrap 5)

## 🏗️ Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Django 5.x |
| Frontend | HTML + Bootstrap 5 |
| Interactivity | Alpine.js |
| Dynamic UI | HTMX |
| Database | SQLite (dev) / PostgreSQL (prod) |

## 🌿 Branch Structure

| Branch | Purpose |
|--------|---------|
| `main` | Stable production code |
| `develop` | Integration branch |
| `feature/tree-ui` | Family tree visual + SVG nodes |
| `feature/admin-panel` | Add/Edit/Delete persons (HTMX) |
| `feature/auth` | Admin login (Django auth) |

## 🚀 Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/Jas2005-ct/Family_Tree.git
cd Family_Tree

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Create superuser
python manage.py createsuperuser

# 6. Load sample data
python manage.py loaddata fixtures/sample_family.json

# 7. Run the server
python manage.py runserver
```

Open: http://127.0.0.1:8000

## 🔐 Admin Access

- **Django Admin:** `/admin/` (superuser)
- **Custom Admin Panel:** `/tree/admin/` (staff users)

## 📁 Project Structure

```
Family_Tree/
├── manage.py
├── requirements.txt
├── family_tree/          ← Django project settings
├── tree/                 ← Main app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/tree/
│   └── static/tree/
└── fixtures/
    └── sample_family.json
```

## 🛠️ Local Development

```bash
# Switch to feature branch
git checkout feature/tree-ui

# After changes, merge to develop
git checkout develop
git merge feature/tree-ui
```

## 📄 License

MIT License — Built with ❤️ as a family gift.
