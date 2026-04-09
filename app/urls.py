from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("checkout/", views.checkout),
    path("webhook/", views.webhook),
]