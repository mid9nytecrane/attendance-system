from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        # Only start the scheduler in the main process (not in manage.py commands
        # like makemigrations, or in the reloader child process).
        import os
        if os.environ.get('RUN_MAIN') != 'true':
            # Production / gunicorn — always start
            # Dev server — RUN_MAIN is set only in the reloader child, so we
            # start in the parent to avoid double-scheduling.
            from .scheduler import start
            start()
