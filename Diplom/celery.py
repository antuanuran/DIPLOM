import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Diplom.settings")  # Diplom - меняем на название каталога

app = Celery("diplom")  # Здесь название не принципиально, просто в логах будет указываться в будущем

app.config_from_object("django.conf:settings", namespace="CELERY")  # Здесь тоже не меняем

app.autodiscover_tasks()
