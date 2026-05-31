# 🌳 Family Tree

An interactive family tree web application built with **Django 5**, **Bootstrap 5**, **Alpine.js**, and **HTMX**.

## ✨ Features

- 🌳 Interactive SVG node-connection family tree
- 👤 Click any node to view person details
- 🔐 Admin panel to add/edit/delete family members
- ⚡ HTMX-powered forms (no page reloads)
- 🏔️ Alpine.js for smooth UI interactions
- 📱 Fully responsive (Bootstrap 5)

## 🚀 Quick Start

```bash
git clone https://github.com/Jas2005-ct/Family_Tree.git
cd Family_Tree
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py loaddata fixtures/sample_family.json
python manage.py runserver
```

Open: http://127.0.0.1:8000
