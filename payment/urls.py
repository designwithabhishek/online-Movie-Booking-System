from django.conf.urls import include, url
from django.contrib import admin
from .views import checkout,payment_success,payment_failure,preprocessingform
from django.urls import path
app_name="payment"

urlpatterns = [
    path('',preprocessingform,name="generateform"),
    path('finalsummary',checkout,name="finalsummary"),
    path('success',payment_success,name="payment_success"),
    path('failure',payment_failure,name="payment_failure")
]