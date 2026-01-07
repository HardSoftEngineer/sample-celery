from celery import Celery

celery_app = Celery(
    "worker",
    broker="redis://sample-celery-redis:6379/0",
    backend="redis://sample-celery-redis:6379/1",
    include=["add_delay"],
)

celery_app.conf.update(
    task_track_started=True,
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
)

celery_app.autodiscover_tasks(["add_delay"])
