from __future__ import absolute_import, unicode_literals
from teste.celery import app


@app.task(bind=True)
def debug_task(self):
    print('called')