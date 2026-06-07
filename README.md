# Family Tree

A Django-powered family tree visualization app with a D3.js force-directed node-link diagram and a Tailwind CSS UI.

## Tech Stack
- **Backend:** Django 5, Django REST Framework
- **Frontend:** Tailwind CSS (CDN), D3.js v7, Lucide icons
- **DB:** PostgreSQL (prod) / SQLite (dev)
- **Deploy:** Render + WhiteNoise

## Quick Start

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_sample_data   # loads 3-generation demo family
python manage.py runserver
```

Visit http://127.0.0.1:8000/

## Project Structure

```
tree/
  models.py          # Person + Relationship
  serializers.py     # DRF serializers
  views.py           # ViewSets + /api/v1/persons/graph-data/
  urls.py            # REST router + template view
  admin.py
  management/commands/seed_sample_data.py
templates/tree/index.html  # D3 + Tailwind SPA
```

## API Endpoints

| Method | URL | Description |
|--------|-----|-------------|
| GET | `/api/v1/persons/` | List all persons |
| POST | `/api/v1/persons/` | Create person |
| GET/PUT/DELETE | `/api/v1/persons/{id}/` | Person detail |
| GET | `/api/v1/persons/graph-data/` | D3 `{nodes, links}` payload |
| GET | `/api/v1/relationships/` | List relationships |
| POST | `/api/v1/relationships/` | Create relationship |
| GET/PUT/DELETE | `/api/v1/relationships/{id}/` | Relationship detail |

## Deployment (Render)

1. Set env vars: `SECRET_KEY`, `DATABASE_URL`, `DEBUG=False`, `ALLOWED_HOSTS`
2. Build command: `pip install -r requirements.txt && python manage.py migrate`
3. Start command: `gunicorn family_tree.wsgi`
4. Add `whitenoise.middleware.WhiteNoiseMiddleware` to `MIDDLEWARE`
5. Set `STATIC_ROOT = BASE_DIR / 'staticfiles'` and run `collectstatic`
