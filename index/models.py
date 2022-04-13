from django.db import models
from base.models import Base


class Contact(Base):

    phone = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    work_wiht_us = models.URLField(null=True, blank=True)
    ios_app = models.URLField(null=True, blank=True)
    android_app = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.phone} | {self.id}"

class ContactUs(Base):

    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    question = models.TextField()

    def __str__(self):
        return f"{self.phone} | {self.name}"


class RequestQuote(Base):

    email = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.id}, {self.email}"

class PartnersImage(models.Model):

    image = models.FileField(upload_to="partners")

    def __str__(self):
        return f"{self.id}"