from django.db import models
from django.db.models import Model
from django.core.validators import MaxValueValidator

# Create your models here.
class Thing(Model):
    name = models.CharField(
        unique = True
        , blank = False
        , max_length = 30
    )

    description = models.CharField(
        unique = False
        , blank = True
        , max_length = 120
    )

    quantity = models.PositiveIntegerField(
        validators = [
            MaxValueValidator(100)
        ]
    )
