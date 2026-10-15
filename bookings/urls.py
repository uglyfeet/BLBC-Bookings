from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("booking/", views.booking, name="booking"),
    path("availability/", views.availability, name="availability"),
    path("verification/", views.verification, name="verification"),
    path("terms/", views.terms, name="terms"),
    path(
        "manage-bookings/",
        views.manage_bookings,
        name="manage_bookings",
    ),
    path(
        "manage-bookings/verification/",
        views.manage_bookings_verification,
        name="manage_bookings_verification",
    ),
    path(
        "manage-bookings/detail/<int:booking_id>/",
        views.manage_booking_detail,
        name="manage_booking_detail",
    ),
    path(
        "manage-bookings/edit/<int:booking_id>/",
        views.edit_booking,
        name="edit_booking",
    ),
    path(
        "manage-bookings/delete/<int:booking_id>/",
        views.delete_booking,
        name="delete_booking",
    ),
]
