from django.urls import path

from contacts.views import ContactPage, sendMail
app_name = 'contacts'

urlpatterns = [
    path('', ContactPage.as_view(), name='contactpage'),
    path('sendmail/', sendMail, name='sendmail'),
]