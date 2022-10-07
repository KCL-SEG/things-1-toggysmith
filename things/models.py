from django.db import models
from django.db.models import Model

# Create your models here.
class Thing(Model):
    name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 512)
    quantity = models.PositiveIntegerField()
