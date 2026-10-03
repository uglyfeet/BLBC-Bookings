from django.contrib import admin
from .models import Customer, Room, Booking


admin.site.register(Customer)
admin.site.register(Room)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "booking_reference",
        "customer",
        "room",
        "date",
        "start_time",
        "end_time",
        "status",
        "fee",
    )
