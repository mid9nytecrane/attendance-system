"""
Background scheduler — auto-closes sessions when their end_time is reached.
Runs inside the Django process via APScheduler (no Celery/Redis needed).
"""
import logging
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from django.utils import timezone

logger = logging.getLogger(__name__)

_scheduler = None


def close_expired_sessions():
    """
    Called every minute. Finds active sessions whose end_time has passed
    and sets is_active = False on each one.
    """
    # Import here to avoid AppRegistryNotReady at startup
    from .models import Session

    now_time = timezone.localtime(timezone.now()).time()
    expired = Session.objects.filter(is_active=True, end_time__isnull=False, end_time__lte=now_time)

    count = expired.count()
    if count:
        expired.update(is_active=False)
        logger.info(f"[scheduler] Auto-closed {count} session(s) at {now_time.strftime('%H:%M')}")


def start():
    global _scheduler
    if _scheduler is not None:
        return  # already running

    _scheduler = BackgroundScheduler(timezone=str(timezone.get_current_timezone()))
    _scheduler.add_job(
        close_expired_sessions,
        trigger=IntervalTrigger(minutes=1),
        id='close_expired_sessions',
        replace_existing=True,
    )
    _scheduler.start()
    logger.info("[scheduler] Started — checking for expired sessions every minute.")
