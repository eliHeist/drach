from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from events.models import Event

from photos.models import Photo

# Create your views here.

class HomePage(TemplateView):
    template_name = "main/home.html"


class AboutPage(TemplateView):
    template_name = "main/about.html"


class PhotoListView(ListView):
    model = Photo
    template_name = "main/gallery.html"

def galleryView(request):
    template_name = "main/gallery.html"
    photos = Photo.objects.all()
    events = Event.objects.all()
    context = {
        'photos':photos,
        'events':events,
    }

    return render(request, template_name, context)



