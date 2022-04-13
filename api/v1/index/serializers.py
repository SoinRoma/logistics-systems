
from rest_framework import serializers

from index.models import ContactUs, RequestQuote


class ContactUsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactUs
        fields = '__all__'


class RequestQuoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = RequestQuote
        fields = '__all__'