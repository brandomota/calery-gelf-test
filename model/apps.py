from django.apps import AppConfig


class ModelConfig(AppConfig):
    name = 'model'

    def ready(self):
        from model import signals