from django.db import models
from base.models import Base
from django.db.models.signals import post_save
from django.dispatch import receiver
from index.mail_service import send_all_mail

class Contact(Base):

    phone = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    work_wiht_us = models.URLField(null=True, blank=True)
    ios_app = models.URLField(null=True, blank=True)
    android_app = models.URLField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.phone} | {self.id}"

class ContactUs(Base):

    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    question = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.phone} | {self.name}"

class Receiver(models.Model):

    email = models.EmailField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.email


class RequestQuote(Base):

    email = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.id}, {self.email}"

class PartnersImage(models.Model):

    image = models.FileField(upload_to="partners")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.id}"


@receiver(post_save, sender=ContactUs)
def send_contact_us_mail(sender, instance, created, **kwargs):
    if created:
        send_all_mail(Receiver.objects.all(), {'contact_us': instance}, 'mail/contact_us.html')
    
@receiver(post_save, sender=RequestQuote)
def send_quote_mail(sender, instance, created, **kwargs):
    if created:
        send_all_mail(Receiver.objects.all(), {'quote': instance}, 'mail/quote.html')
    
