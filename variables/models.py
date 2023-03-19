from django.db import models

# Create your models here.
class Variable(models.Model):
    name = models.CharField(unique=True, max_length=50)
    image = models.ImageField()
    value = models.CharField(max_length=2000, null=True, blank=True)
    text = models.TextField(blank=True, null=True)