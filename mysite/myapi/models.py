from django.db import models

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Spell(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()

    def __str__(self):
        return self.name