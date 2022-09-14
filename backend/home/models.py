from django.conf import settings
from django.db import models


class Tester(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=256,
    )
