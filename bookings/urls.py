from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("booking/", views.booking, name="booking"),
    path("availability/", views.availability, name="availability"),
    path("verification/", views.verification, name="verification"),
]
