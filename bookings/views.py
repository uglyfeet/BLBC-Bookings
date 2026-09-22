from datetime import date, datetime
from decimal import Decimal
from django.contrib import messages
from django.shortcuts import render, redirect

from .models import Booking, Customer, Room


def home(request):

    rooms = Room.objects.filter(available=True)

    return render(request, "bookings/home.html", {"rooms": rooms})


def booking(request):

    if request.method == "POST":
        room = Room.objects.get(id=request.POST.get("room"))
        date_value = request.POST.get("date")
        start_time = request.POST.get("start_time")
        end_time = request.POST.get("end_time")

        booking_date = datetime.strptime(
            date_value, "%Y-%m-%d"
        ).date()

        if booking_date < date.today():
            messages.error(
                request,
                "You cannot book a date in the past.",
            )
        elif (
            booking_date == date.today()
            and start_time <= datetime.now().strftime("%H:%M")
        ):
            messages.error(
                request,
                "You cannot book a time that has already passed.",
            )
        elif end_time <= start_time:
            messages.error(
                request,
                "The end time must be after the start time.",
            )
        else:
            overlapping_booking = Booking.objects.filter(
                room=room,
                date=date_value,
                start_time__lt=end_time,
                end_time__gt=start_time,
            ).exists()

            if overlapping_booking:
                messages.error(
                    request,
                    "This room is already booked for the selected time.",
                )
            else:
                customer = Customer.objects.create(
                    name=request.POST.get("name"),
                    phone=request.POST.get("phone"),
                    email=request.POST.get("email"),
                )

                start = datetime.strptime(start_time, "%H:%M")
                end = datetime.strptime(end_time, "%H:%M")

                duration = Decimal(
                    (end - start).total_seconds()
                ) / Decimal(3600)

                fee = duration * room.hourly_rate

                Booking.objects.create(
                    customer=customer,
                    room=room,
                    date=date_value,
                    start_time=start_time,
                    end_time=end_time,
                    fee=fee,
                )

                messages.success(
                    request,
                    f"Your booking request has been submitted. "
                    f"Duration: {duration} hours. "
                    f"Fee: £{fee:.2f}. "
                    f"Your booking is currently pending confirmation.",
                )
                return redirect("booking")

    rooms = Room.objects.filter(available=True)

    return render(request, "bookings/booking.html", {"rooms": rooms})
