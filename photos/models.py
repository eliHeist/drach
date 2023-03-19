from django.db import models

# Create your models here.
class Photo(models.Model):
    image = models.ImageField()
    tags = models.ManyToManyField('Tag', related_name='photos', blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)


class Tag(models.Model):
    name = models.CharField(max_length=100)


class Video(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    video = models.FileField()
    tags = models.ManyToManyField(Tag, related_name='videos', blank=True)