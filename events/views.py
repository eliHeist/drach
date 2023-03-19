from django.shortcuts import render
from django.views.generic import DetailView

from events.models import Event

# Create your views here.

class EventDetailView(DetailView):
    model = Event
    context_object_name = 'event'
    template_name = "events/detail.html"
