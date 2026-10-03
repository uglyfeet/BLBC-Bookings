from datetime import datetime
from decimal import Decimal

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

    def save_model(self, request, obj, form, change):
        start = datetime.combine(obj.date, obj.start_time)
        end = datetime.combine(obj.date, obj.end_time)

        duration = Decimal(
            (end - start).total_seconds()
        ) / Decimal(3600)

        obj.fee = duration * obj.room.hourly_rate

        super().save_model(request, obj, form, change)
