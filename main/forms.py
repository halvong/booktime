from django.core.mail import send_mail
from django import forms
import logging

logger = logging.getLogger(__name__)

class ContactForm(forms.Form):

    name = forms.CharField(label='Your name', max_length=100)

    message = forms.CharField(max_length=600, widget=forms.Textarea)

    def send_mail(self):
        #self.cleaned_data["name"],
        #self.cleaned_data["message"],
        logger.info("Sending email to customer service")
        message = "From: {0}\n{1}".format(
            self.name,
            self.message,
        )
        #print ("sendmail",message)
        send_mail("Site booktime", message, "no-reply@booktime.com", ["hvong@yahoo.com"], fail_silently=False,)