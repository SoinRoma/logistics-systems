from django.contrib import admin
from .models import Contact, ContactUs, RequestQuote, PartnersImage, Receiver
# Register your models here.

admin.site.register(Contact)
admin.site.register(ContactUs)
admin.site.register(RequestQuote)
admin.site.register(PartnersImage)
admin.site.register(Receiver)
