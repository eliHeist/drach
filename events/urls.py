from django.urls import path

from events.views import EventDetailView

app_name = 'events'

urlpatterns = [
    path('<int:pk>/', EventDetailView.as_view(), name='detail'),
]