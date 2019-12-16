from django.db import models

class Object(models.Model):
    number = models.IntegerField(null=True,blank=True)
