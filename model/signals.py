from django.db.models.signals import post_save
from django.dispatch import receiver

from model.models import Object
from .tasks import debug_task


@receiver(post_save,sender=Object)
def call_celery(sender, instance, **kwargs):
    debug_task.delay()

