from django.contrib import messages
from django.shortcuts import render, redirect

from .models import Booking, Customer, Room


def home(request):

    rooms = Room.objects.filter(available=True)

    return render(request, "bookings/home.html", {"rooms": rooms})


def booking(request):

    if request.method == "POST":
        customer = Customer.objects.create(
            name=request.POST.get("name"),
            phone=request.POST.get("phone"),
            email=request.POST.get("email"),
        )

        Booking.objects.create(
            customer=customer,
            room=Room.objects.get(id=request.POST.get("room")),
            date=request.POST.get("date"),
            start_time=request.POST.get("start_time"),
            end_time=request.POST.get("end_time"),
        )

        messages.success(
            request,
            "Your booking request has been submitted and is currently"
            " pending confirmation.",
        )

        return redirect("booking")

    rooms = Room.objects.filter(available=True)

    return render(request, "bookings/booking.html", {"rooms": rooms})
