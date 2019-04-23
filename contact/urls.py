from django.contrib import admin
from django.urls import path
from . import views
urlpatterns=[
    path('contact/',views.contactUs,name='contact'),
    path('faq/',views.faq,name='faq'),
    path('contact1/', views.contactUs1, name='contact1'),
    path('faq1/', views.faq1, name='faq1'),

]