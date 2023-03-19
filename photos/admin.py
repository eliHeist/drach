from django.contrib import admin

from photos.models import Photo, Tag, Video
from django.utils.html import format_html

@admin.register(Photo) 
class PhotoAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html(f'<img src="{obj.image.url}" class="img-fluid" style="max-width:200px;" />')

    image_tag.short_description = 'Current image'

    list_display = ['image_tag',]
    # fields = ["image_tag"]
    readonly_fields = ["image_tag"]
admin.site.register(Tag)


admin.site.register(Video)