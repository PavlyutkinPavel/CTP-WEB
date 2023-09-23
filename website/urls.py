from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('about/faq', faq, name='faq'),
    path('about/requisites', requisites, name='requisites'),
    path('about/contacts', contacts, name='contacts'),
    path('about/privacy-policy', privacy_policy, name='privacy-policy'),
    path('about/coupons', coupons, name='coupons'),
    path('weather/', get_weather, name='weather'),
    path('gender/', get_gender, name='gender'),
]
