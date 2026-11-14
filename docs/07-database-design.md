# Database Design

## Overview

The BLBC Booking System uses a relational database to store customer details, room information and booking requests.

The database uses three main models: Customer, Room and Booking. These models are linked using foreign key relationships to reduce duplicated information and maintain data consistency.

## Customer

| Field | Purpose |
|---|---|
| ID | Unique customer number |
| Name | Customer name |
| Phone | Customer telephone number |
| Email | Customer email address |
| Verification Code | Email verification code |
| Email Verified | Records whether the email has been verified |

## Room

| Field | Purpose |
|---|---|
| ID | Unique room number |
| Name | Name of the room |
| Description | Description of the room |
| Capacity | Maximum number of people |
| Hourly Rate | Cost per hour |
| Available | Records whether the room is available |
| Image | Room photograph |

## Booking

| Field | Purpose |
|---|---|
| ID | Unique booking number |
| Customer | Links the booking to a customer |
| Room | Links the booking to a room |
| Date | Booking date |
| Start Time | Booking start time |
| End Time | Booking finish time |
| Booking Reference | Unique booking reference |
| Status | Pending, Approved, Rejected or Cancelled |
| Fee | Total booking cost |

## Database Relationships

The database uses the following relationships:

- **Customer to Booking:** One customer can have many bookings. Each booking belongs to one customer.
- **Room to Booking:** One room can have many bookings over time. Each booking is for one room.

Both relationships use foreign keys in the Booking model. This allows customer and room information to be stored once and linked to multiple bookings.

If a customer or room is deleted, its associated bookings are also deleted through the configured cascade behaviour.

CUSTOMER (1) -------- (Many) BOOKING (Many) -------- (1) ROOM


## Administrator Accounts

Administrator accounts are managed using Django's built-in authentication system. Django stores account information and securely hashes passwords rather than storing them as plain text.

The Django administration interface allows authorised administrators to manage rooms, customers and bookings.