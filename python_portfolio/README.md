# Python Developer Portfolio

A production-ready personal website for a Python/Django developer. Content is editable from Django Admin, the contact form stores inquiries in the database, and the project is configured for Render with Gunicorn, WhiteNoise, and PostgreSQL.

## Features

- Single-page portfolio with hero, about, skills, experience, projects, education, certifications, services, GitHub stats, contact, and footer
- Dark/light theme persisted in `localStorage`
- Responsive layout and accessible navigation
- Dynamic content via Django models and admin
- Contact form with CSRF, validation, and basic spam checks
- SEO metadata, `robots.txt`, and `sitemap.xml`
- SQLite for local development and PostgreSQL in production
- WhiteNoise static files and Gunicorn for Render

## Tech stack

- Python 3.12, Django 5.2
- HTML5, CSS3, JavaScript
- SQLite / PostgreSQL
- WhiteNoise, Gunicorn, dj-database-url
- Render for hosting

## Project structure

```text
manage.py
config/                 # Django project settings and URLs
portfolio_app/          # Models, views, templates, static files
media/                  # User-uploaded resume/project images
staticfiles/            # collectstatic output (not committed)
requirements.txt
build.sh
render.yaml
.env.example
```

## Local installation

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

macOS / Linux:

```bash
source venv/bin/activate
```

```bash
pip install -r requirements.txt
copy .env.example .env
```

On macOS/Linux use `cp .env.example .env`. Edit `.env` and set a unique `SECRET_KEY`.

## Environment variables

| Variable | Purpose |
| --- | --- |
| `SECRET_KEY` | Django secret key (required in production) |
| `DEBUG` | `True` locally, `False` in production |
| `ALLOWED_HOSTS` | Comma-separated hosts |
| `CSRF_TRUSTED_ORIGINS` | Comma-separated origins, including `https://` |
| `DATABASE_URL` | Postgres URL in production; omit locally to use SQLite |
| `SECURE_SSL_REDIRECT` | `True` in production |
| `RENDER_EXTERNAL_URL` | Set automatically on Render; used for CSRF/hosts |

See `.env.example` for a local template.

## Database setup

Local development uses SQLite (`db.sqlite3`) when `DATABASE_URL` is unset.

Production uses PostgreSQL through `DATABASE_URL`.

```bash
python manage.py migrate
python manage.py seed_portfolio
python manage.py createsuperuser
python manage.py runserver
```

Placeholder content is also created automatically after the first migration.

Open http://127.0.0.1:8000/

## Django Admin

- URL: http://127.0.0.1:8000/admin/
- Update name, links, skills, experience, projects, education, certifications, services, and contact messages there.

## Static files

```bash
python manage.py collectstatic
```

WhiteNoise serves collected files in production.

## Resume

Replace `portfolio_app/static/resume/YOUR_RESUME.pdf` with your PDF, or upload a file on **Site profile** in admin. Keep the filename in mind if you change the static path.

## Customize portfolio information

Search the project or use Django Admin to replace:

- `[YOUR NAME]`
- `[YOUR EMAIL]`
- `[YOUR LOCATION]`
- `[YOUR GITHUB]`
- `[YOUR LINKEDIN]`
- `[YOUR PHONE]`
- `[YOUR RESUME]`
- `[YOUR DEGREE]`, `[YOUR UNIVERSITY]`, `[COMPANY NAME]`, `[CERTIFICATION NAME]`

## GitHub setup

```bash
git init
git add .
git commit -m "Add Django developer portfolio"
git branch -M main
git remote add origin https://github.com/[YOUR GITHUB]/[REPO].git
git push -u origin main
```

Do not commit `.env` or `db.sqlite3`.

## Render deployment

1. Push this repository to GitHub.
2. In Render, create a **Blueprint** from `render.yaml`, or create a Web Service and a PostgreSQL database manually.
3. Use:
   - Build command: `./build.sh`
   - Start command: `gunicorn config.wsgi:application --bind 0.0.0.0:$PORT`
4. Set environment variables:
   - `SECRET_KEY` (Render can generate this)
   - `DEBUG=False`
   - `ALLOWED_HOSTS=.onrender.com,your-custom-domain`
   - `CSRF_TRUSTED_ORIGINS=https://your-service.onrender.com`
   - `DATABASE_URL` from the Render Postgres instance
   - `SECURE_SSL_REDIRECT=True`
5. After the first deploy, create a superuser from the Render shell:

```bash
python manage.py createsuperuser
```

6. Open `/admin/` and replace placeholder content.

Render no longer offers a long-term free Postgres plan on every account. Use the database plan available to you, then attach `DATABASE_URL`.

If you deploy without the Blueprint, make `build.sh` executable (`chmod +x build.sh`).

## How to run tests

```bash
python manage.py test
```
