# from main.models import Subscriber
from django import forms
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.conf import settings


# class NewsletterForm(forms.ModelForm):
#     class Meta:
#         model = Subscriber
#         fields = (
#             'email',
#         )

class ContactForm(forms.Form):
    your_name = forms.CharField(required=False)
    your_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    your_message = forms.CharField(widget=forms.Textarea, required=True)
    # message = forms.CharField(widget=forms.Textarea, required=True)

    def send_email(self, subject, email, text, name):
        subject = subject
        email = email
        text = text
        name = name
        message = f"{name}: {email}\n\n{text}"

        try:
            send_mail(subject, message, settings.EMAIL_HOST_USER, ['amartislab@gmail.com','elijahtriumph@amartislab.com','support@amartislab.com'], fail_silently=False)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')


# class ContactForm(forms.Form):
#     your_name = forms.CharField(required=False)
#     your_email = forms.EmailField(required=True)
#     subject = forms.CharField(required=True)
#     your_message = forms.CharField(widget=forms.Textarea, required=True)
#     # message = forms.CharField(widget=forms.Textarea, required=True)

#     def send_email(self):
#         subject = self.cleaned_data.get('subject')
#         email = self.cleaned_data.get('your_email')
#         text = self.cleaned_data.get('your_message')
#         name = self.cleaned_data.get('your_name')
#         message = f"{name}: {email}\n\n{text}"
#         print(message)

#         try:
#             send_mail(subject, message, settings.EMAIL_HOST_USER, ['amartissebaggala@gmail.com','eliyang256@outlook.com', 'kayimaoscul@gmail.com', 'ogocharles231@gmail.com'], fail_silently=False)
#         except BadHeaderError:
#             return HttpResponse('Invalid header found.')