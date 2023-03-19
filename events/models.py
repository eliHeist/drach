from statistics import mode
from django.db import models

from photos.models import Photo, Video

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    video = models.ForeignKey(Video, on_delete=models.SET_NULL, null=True, blank=True)
    featured_image = models.ForeignKey(Photo, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title


class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='photos')
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)


class EventVideo(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='videos')
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
