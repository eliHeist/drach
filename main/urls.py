from django.urls import path

from main.views import AboutPage, HomePage, galleryView

app_name = 'main'

urlpatterns = [
    path('', HomePage.as_view(), name='homepage'),
    path('gallery/', galleryView, name='gallery'),
    path('about/', AboutPage.as_view(), name='aboutpage'),
]