# Tech Stack

## Backend
- **Python** with **Django 5.2.4**
- **SQLite** (default DB via `db.sqlite3`) — suitable for development
- Django's built-in auth system (`django.contrib.auth`)

## Frontend
- **Tailwind CSS** — loaded via CDN (`https://cdn.tailwindcss.com`)
- **Alpine.js** — loaded via CDN (`https://unpkg.com/alpinejs`), used for lightweight interactivity
- Django template engine with template inheritance (`{% extends %}`, `{% block %}`, `{% include %}`)

## No build system
There is no Node.js, bundler, or package manager. CSS and JS are CDN-only. Do not introduce npm/webpack/vite unless explicitly requested.

## Common Commands

```bash
# Run development server
python manage.py runserver

# Create and apply migrations
python manage.py makemigrations
python manage.py migrate

# Create a superuser
python manage.py createsuperuser

# Open Django shell
python manage.py shell

# Run tests
python manage.py test
```

## Settings Notes
- `DEBUG = True` — development only
- Templates directory is configured globally: `BASE_DIR / 'templates'`
- `DEFAULT_AUTO_FIELD = BigAutoField`
- Timezone: UTC
