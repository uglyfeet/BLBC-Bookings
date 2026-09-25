from datetime import date, datetime, timedelta
from decimal import Decimal
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Booking, Customer, Room
import random


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
                verification_code = str(random.randint(100000, 999999))
                request.session["verification_code"] = verification_code
                request.session["verification_expiry"] = (
                    datetime.now().timestamp() + 600
                )
                request.session["booking_data"] = {
                    "name": request.POST.get("name"),
                    "phone": request.POST.get("phone"),
                    "email": request.POST.get("email"),
                    "room": room.id,
                    "date": date_value,
                    "start_time": start_time,
                    "end_time": end_time,
                }

                send_mail(
                    "BLBC Email Verification",
                    f"Your verification code is: {verification_code}",
                    "welch.antony@gmail.com",
                    [request.POST.get("email")],
                    )

                start = datetime.strptime(start_time, "%H:%M")
                end = datetime.strptime(end_time, "%H:%M")

                duration = Decimal(
                    (end - start).total_seconds()
                ) / Decimal(3600)
                fee = duration * room.hourly_rate
                request.session["booking_data"]["fee"] = str(fee)
                return redirect("verification")

    rooms = Room.objects.filter(available=True)

    return render(request, "bookings/booking.html", {"rooms": rooms})


def availability(request):

    rooms = Room.objects.filter(available=True)

    selected_date = request.GET.get("date")

    times = [
        "08:00",
        "08:30",
        "09:00",
        "09:30",
        "10:00",
        "10:30",
        "11:00",
        "11:30",
        "12:00",
        "12:30",
        "13:00",
        "13:30",
        "14:00",
        "14:30",
        "15:00",
        "15:30",
        "16:00",
        "16:30",
        "17:00",
        "17:30",
        "18:00",
        "18:30",
        "19:00",
        "19:30",
        "20:00",
        "20:30",
        "21:00",
        "21:30",
        "22:00",
    ]

    bookings = Booking.objects.filter(
        date=selected_date
    ).order_by("start_time")

    booked_slots = []

    for booking in bookings:
        current_time = booking.start_time

        while current_time < booking.end_time:
            booked_slots.append(
                {
                    "room": booking.room.id,
                    "time": current_time.strftime("%H:%M"),
                }
            )

            current_time = (
                datetime.combine(
                    booking.date,
                    current_time,
                )
                + timedelta(minutes=30)
            ).time()

    return render(
        request,
        "bookings/availability.html",
        {
            "rooms": rooms,
            "bookings": bookings,
            "times": times,
            "booked_slots": booked_slots,
        },
    )


def verification(request):
    if request.method == "POST":
        code = request.POST.get("code")
        saved_code = request.session.get("verification_code")
        expiry = request.session.get("verification_expiry")
        if expiry and datetime.now().timestamp() > expiry:
            messages.error(
                request,
                (
                    "Your verification code has expired. "
                    "Please request a new code."
                ),
            )
            return redirect("booking")

        if code == saved_code:
            booking_data = request.session.get("booking_data")

            customer = Customer.objects.create(
                name=booking_data["name"],
                phone=booking_data["phone"],
                email=booking_data["email"],
                email_verified=True,
            )

            room = Room.objects.get(id=booking_data["room"])

            Booking.objects.create(
                customer=customer,
                room=room,
                date=booking_data["date"],
                start_time=booking_data["start_time"],
                end_time=booking_data["end_time"],
                fee=booking_data["fee"],
            )

            del request.session["verification_code"]
            del request.session["booking_data"]
            del request.session["verification_expiry"]

            messages.success(
                request,
                (
                    "Your email has been verified and your booking "
                    "has been submitted."
                ),
            )

            return redirect("booking")

        messages.error(
            request,
            "Invalid verification code.",
        )

    return render(request, "bookings/verification.html")
