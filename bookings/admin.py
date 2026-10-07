from datetime import datetime, date, timedelta
from decimal import Decimal

from django.contrib import admin

from .models import Customer, Room, Booking


admin.site.register(Customer)
admin.site.register(Room)


class UpcomingBookingsFilter(admin.SimpleListFilter):
    """Filter bookings to show only those in the next 7 days."""
    title = "Upcoming"
    parameter_name = "upcoming"

    def lookups(self, request, model_admin):
        """Return the filter options for the admin interface."""
        return (
            ("next_7_days", "Next 7 days"),
        )

    def queryset(self, request, queryset):
        """Return the filtered queryset based on the selected filter."""
        if self.value() == "next_7_days":
            today = date.today()
            next_week = today + timedelta(days=7)

            return queryset.filter(
                date__gte=today,
                date__lte=next_week,
            )

        return queryset


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """Admin interface for the Booking model."""
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

    list_filter = ("date", "status", UpcomingBookingsFilter)

    search_fields = (
        "booking_reference",
        "customer__name",
        "customer__email",
    )

    def save_model(self, request, obj, form, change):
        """Calculate the fee based on the duration
            and hourly rate before saving."""
        start = datetime.combine(obj.date, obj.start_time)
        end = datetime.combine(obj.date, obj.end_time)

        duration = Decimal(
            (end - start).total_seconds()
        ) / Decimal(3600)

        obj.fee = duration * obj.room.hourly_rate

        super().save_model(request, obj, form, change)
