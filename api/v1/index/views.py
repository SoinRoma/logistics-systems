from rest_framework.generics import CreateAPIView

from api.v1.index.serializers import RequestQuoteSerializer, ContactUsSerializer


class RequestQuoteView(CreateAPIView):
    serializer_class = RequestQuoteSerializer


class ContactUsView(CreateAPIView):
    serializer_class = ContactUsSerializer
