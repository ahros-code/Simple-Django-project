from django.db import models

class suzlar(models.Model):
    inglizcha = models.CharField(max_length=128)
    uzbekcha = models.CharField(max_length=128)
