from datetime import date, datetime, timedelta
from decimal import Decimal
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from .models import Booking, Customer, Room
import random


def home(request):
    """Display the home page with available rooms."""

    rooms = Room.objects.filter(available=True)

    return render(request, "bookings/home.html", {"rooms": rooms})


def booking(request):
    """Display the booking page and handle booking submissions."""
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
    """Display the availability of rooms for a selected date."""
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
    """Display the verification page and handle verification submissions."""
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

            booking_reference = str(random.randint(100000, 999999))

            Booking.objects.create(
                customer=customer,
                room=room,
                date=booking_data["date"],
                start_time=booking_data["start_time"],
                end_time=booking_data["end_time"],
                booking_reference=booking_reference,
                fee=booking_data["fee"],
            )

            send_mail(
                "BLBC Booking Confirmation",
                (
                    f"Your booking has been received.\n\n"
                    f"Booking reference: {booking_reference}\n"
                    f"Room: {room.name}\n"
                    f"Date: {booking_data['date']}\n"
                    f"Start time: {booking_data['start_time']}\n"
                    f"End time: {booking_data['end_time']}\n"
                    f"Fee: £{Decimal(booking_data['fee']):.2f}\n\n"
                    "Your booking is currently pending approval."
                ),
                "welch.antony@gmail.com",
                [booking_data["email"]],
            )

            del request.session["verification_code"]
            del request.session["booking_data"]
            del request.session["verification_expiry"]

            messages.success(
                request,
                (
                    "Your booking has been submitted. "
                    f"Your booking reference is {booking_reference}."
                ),
            )

            return redirect("booking")

        messages.error(
            request,
            "Invalid verification code.",
        )

    return render(request, "bookings/verification.html")


def terms(request):
    """Display the terms and conditions page."""
    return render(request, "bookings/terms.html")


def manage_bookings(request):
    """Find a booking using the customer's email and reference."""

    if request.method == "POST":
        email = request.POST.get("email", "").strip()
        booking_reference = request.POST.get(
            "booking_reference", ""
        ).strip()

        booking = Booking.objects.filter(
            customer__email__iexact=email,
            booking_reference=booking_reference,
        ).first()

        if booking:
            verification_code = str(
                random.randint(100000, 999999)
            )

            request.session["manage_booking_code"] = (
                verification_code
            )
            request.session["manage_booking_expiry"] = (
                datetime.now().timestamp() + 600
            )
            request.session["manage_booking_id"] = booking.id

            send_mail(
                "BLBC Booking Verification",
                f"Your verification code is: {verification_code}",
                "welch.antony@gmail.com",
                [booking.customer.email],
            )

            return redirect("manage_bookings_verification")

        messages.error(
            request,
            "We could not find a booking matching those details.",
        )

    return render(request, "bookings/manage_bookings.html")


def manage_bookings_verification(request):
    """Verify the customer's access to an existing booking."""

    if request.method == "POST":
        code = request.POST.get("code", "").strip()
        saved_code = request.session.get("manage_booking_code")
        expiry = request.session.get("manage_booking_expiry")

        if not expiry or datetime.now().timestamp() > expiry:
            messages.error(
                request,
                "Your verification code has expired. Please try again.",
            )
            return redirect("manage_bookings")

        if code == saved_code and saved_code:
            booking_id = request.session.get("manage_booking_id")

            if not Booking.objects.filter(id=booking_id).exists():
                messages.error(request, "Booking not found.")
                return redirect("manage_bookings")

            request.session["authorised_booking_id"] = booking_id
            request.session["authorised_booking_expiry"] = (
                datetime.now().timestamp() + 600
            )
            del request.session["manage_booking_code"]
            del request.session["manage_booking_expiry"]
            del request.session["manage_booking_id"]

            return redirect(
                "manage_booking_detail",
                booking_id=booking_id,
            )

        messages.error(request, "Invalid verification code.")

    return render(
        request,
        "bookings/manage_bookings_verification.html",
    )


def edit_booking(request, booking_id):
    """Allow a verified customer to edit their booking."""

    if (
        request.session.get("authorised_booking_id") != booking_id
        or datetime.now().timestamp()
        > request.session.get("authorised_booking_expiry", 0)
    ):
        messages.error(
            request,
            "Please verify your booking details again.",
        )
        return redirect("manage_bookings")

    booking = get_object_or_404(Booking, id=booking_id)
    rooms = Room.objects.filter(available=True)

    times = []
    current_time = datetime.strptime("08:00", "%H:%M")
    closing_time = datetime.strptime("22:00", "%H:%M")

    while current_time <= closing_time:
        times.append(current_time.strftime("%H:%M"))
        current_time += timedelta(minutes=30)

    if request.method == "POST":
        date_value = request.POST.get("date", "")
        room_id = request.POST.get("room", "")
        start_time = request.POST.get("start_time", "")
        end_time = request.POST.get("end_time", "")

        try:
            booking_date = datetime.strptime(
                date_value, "%Y-%m-%d"
            ).date()
            start = datetime.strptime(start_time, "%H:%M")
            end = datetime.strptime(end_time, "%H:%M")
            room = get_object_or_404(
                rooms, id=room_id
            )
        except (ValueError, TypeError):
            messages.error(
                request,
                "Please enter valid booking details.",
            )
            return render(
                request,
                "bookings/edit_booking.html",
                {
                    "booking": booking,
                    "rooms": rooms,
                    "times": times,
                },
            )

        if booking_date < date.today():
            messages.error(
                request, "You cannot choose a past date."
            )

        elif (
            booking_date == date.today()
            and start_time <= datetime.now().strftime("%H:%M")
        ):
            messages.error(
                request,
                "You cannot choose a time that has already passed.",
            )

        elif end_time <= start_time:
            messages.error(
                request,
                "The end time must be after the start time.",
            )

        elif Booking.objects.filter(
            room=room,
            date=booking_date,
            start_time__lt=end_time,
            end_time__gt=start_time,
        ).exclude(id=booking.id).exists():
            messages.error(
                request,
                "That room is already booked for this time.",
            )

        else:
            duration = Decimal(
                str((end - start).total_seconds() / 3600)
            )
            booking.room = room
            booking.date = booking_date
            booking.start_time = start_time
            booking.end_time = end_time
            booking.fee = duration * room.hourly_rate
            booking.status = "Pending"
            booking.save()

            send_mail(
                "BLBC Booking Confirmation - Amended",
                (
                    "Your booking has been amended successfully.\n\n"
                    f"Booking reference: {booking.booking_reference}\n"
                    f"Room: {booking.room.name}\n"
                    f"Date: {booking.date}\n"
                    f"Start time: {booking.start_time}\n"
                    f"End time: {booking.end_time}\n"
                    f"Fee: £{booking.fee:.2f}\n\n"
                    "Your amended booking is now pending approval."
                ),
                "welch.antony@gmail.com",
                [booking.customer.email],
            )
            request.session.pop("authorised_booking_id", None)
            request.session.pop("authorised_booking_expiry", None)

            messages.success(
                request,
                "Your booking has been updated and is pending approval.",
            )
            return redirect("manage_bookings")

    return render(
        request,
        "bookings/edit_booking.html",
        {
            "booking": booking,
            "rooms": rooms,
            "times": times,
        },
    )


def manage_booking_detail(request, booking_id):
    """Show a verified customer's booking details."""

    if (
        request.session.get("authorised_booking_id") != booking_id
        or datetime.now().timestamp()
        > request.session.get("authorised_booking_expiry", 0)
    ):
        messages.error(
            request,
            "Please verify your booking details again.",
        )
        return redirect("manage_bookings")

    booking = get_object_or_404(Booking, id=booking_id)

    return render(
        request,
        "bookings/manage_booking_detail.html",
        {"booking": booking},
    )


def delete_booking(request, booking_id):
    """Allow a verified customer to delete their booking."""

    if request.method != "POST":
        return redirect(
            "manage_booking_detail",
            booking_id=booking_id,
        )

    if (
        request.session.get("authorised_booking_id") != booking_id
        or datetime.now().timestamp()
        > request.session.get("authorised_booking_expiry", 0)
    ):
        messages.error(
            request,
            "Please verify your booking details again.",
        )
        return redirect("manage_bookings")

    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()

    request.session.pop("authorised_booking_id", None)
    request.session.pop("authorised_booking_expiry", None)

    messages.success(request, "Your booking has been deleted.")

    return redirect("manage_bookings")
