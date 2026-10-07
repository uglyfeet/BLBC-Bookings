from django.db import models


class Customer(models.Model):
    """Model representing a customer."""
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    verification_code = models.CharField(max_length=6, blank=True)
    email_verified = models.BooleanField(default=False)

    def __str__(self):
        """Return the string representation of the customer."""
        return self.name


class Room(models.Model):
    """Model representing a room."""
    name = models.CharField(max_length=100)
    description = models.TextField()
    capacity = models.PositiveIntegerField()
    hourly_rate = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to="room_images/", blank=True, null=True)

    def __str__(self):
        """Return the string representation of the room."""
        return self.name


class Booking(models.Model):
    """Model representing a booking."""
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    booking_reference = models.CharField(max_length=10, unique=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ("Pending", "Pending"),
            ("Approved", "Approved"),
            ("Rejected", "Rejected"),
            ("Cancelled", "Cancelled"),
        ],
        default="Pending",
    )
    fee = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        """Return the string representation of the booking."""
        return f"{self.customer} - {self.room} - {self.date}"
