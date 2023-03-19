from django.conf import settings
from django.core.mail import send_mail
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from django.views.generic import TemplateView, FormView

from contacts.forms import ContactForm
from contacts.models import Receipient


# Create your views here.
class ContactPage(FormView):
   form_class = ContactForm
   success_url = '/contact/success/'
   template_name = "contacts/contactpage.html"


@api_view(['POST'])
def sendMail(request):
   if request.method == 'POST':
      data = request.data
      print(data)
      message = f"Name: {data.get('name')}\nPhone Number: {data.get('phone')}\nEmail: {data.get('email')}\nWants a(n) {data.get('session')} session ({data.get('eventName')}) on {data.get('date')}\nMore info: {data.get('moreInfo')}"
      print("\n\nmessage\n"+message)
      receipients = Receipient.objects.all()

      try:
         send_mail(
            subject=data.get('session'),
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[receipient.email for receipient in receipients]
         )

         return Response('SUCCESS')
      except Exception as e:
         print(f'Exception: {e}')
         return Response('Failed')