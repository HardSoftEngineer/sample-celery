import time 

from add_delay.celery_app import celery_app


@celery_app.task(bind=True)
def add(self, a, b):
    return a + b

@celery_app.task(bind=True)
def add_slow_task(self, a, b, seconds=10):
    for i in range(seconds):
        time.sleep(1)
        self.update_state(
            state="PROGRESS",
            meta={"current": i + 1, "total": seconds},
        )
    return a + b
