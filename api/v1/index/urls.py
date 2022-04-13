from django.urls import path
from .views import ContactUsView, RequestQuoteView

app_name = 'api'

urlpatterns = [
    path('create/', ContactUsView.as_view(),  name = 'create_contact_us'),
    path('create/email/', RequestQuoteView.as_view(),  name = 'create_email'),

]