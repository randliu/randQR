from django.contrib import admin
from django.urls import path
from str2QR import views

urlpatterns = [
    path('/', views.qr),
]
