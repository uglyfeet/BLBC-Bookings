from django.shortcuts import render
from .models import Room


def home(request):
    rooms = Room.objects.filter(available=True)
    return render(request, "bookings/home.html", {"rooms": rooms})