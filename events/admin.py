from django.contrib import admin

from events.models import Event, EventImage, EventVideo

# Register your models here.
class VideoInline(admin.TabularInline):
    model = EventVideo

class ImageInline(admin.TabularInline):
    model = EventImage

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    class Meta:
        fields = '__all__'
    inlines = [VideoInline, ImageInline]