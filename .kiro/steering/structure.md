# Project Structure

```
attendance_app/                  # Project root
├── attendance_app/              # Django project package (settings, root URLs, wsgi/asgi)
│   ├── settings.py
│   ├── urls.py                  # Root URL config — includes core.urls at '/'
│   ├── wsgi.py
│   └── asgi.py
├── core/                        # Primary Django app — all attendance logic lives here
│   ├── models.py                # Data models
│   ├── views.py                 # View functions (function-based views preferred)
│   ├── urls.py                  # App-level URL patterns
│   ├── admin.py                 # Admin registrations
│   ├── tests.py                 # App tests
│   └── migrations/              # Auto-generated migration files
├── templates/                   # Global templates directory
│   └── core/
│       ├── base.html            # Base layout — all pages extend this
│       ├── home.html
│       └── partials/            # Reusable HTML fragments (included via {% include %})
│           └── navbar.html
├── db.sqlite3                   # SQLite database (dev only, not committed to production)
└── manage.py
```

## Conventions

- **All new Django apps** should be registered in `INSTALLED_APPS` in `settings.py`
- **URL routing**: app-level `urls.py` files are included from the root `attendance_app/urls.py`
- **Views**: use function-based views (FBVs) — the existing pattern uses `def view_name(request)`
- **Templates**: 
  - All templates live in `templates/` at the project root
  - App templates go under `templates/<app_name>/`
  - Reusable fragments go in `templates/<app_name>/partials/`
  - All page templates extend `core/base.html` using `{% extends "core/base.html" %}`
- **Models**: define in `core/models.py`; always run `makemigrations` + `migrate` after changes
- **Admin**: register models in `core/admin.py` using `admin.site.register()`
- **Static files**: no static directory yet — CSS/JS loaded via CDN in `base.html`
