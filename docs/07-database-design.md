# Database Design

## Overview

The BLBC Booking System will use a relational database to store information about rooms, booking requests and administrator accounts. The database has been designed to organise data efficiently while preventing duplicate information.

The system will use three main tables:

### Rooms

| Field       | Purpose                  |
| ----------- | ------------------------ |
| Room ID     | Unique room number       |
| Room Name   | Name of the room         |
| Description | Description of the room  |
| Capacity    | Maximum number of people |
| Hourly Rate | Cost per hour            |
| Image       | Room photograph          |

### Bookings

| Field         | Purpose                       |
| ------------- | ----------------------------- |
| Booking ID    | Unique booking number         |
| Customer Name | Name of the customer          |
| Email         | Customer email address        |
| Phone         | Customer phone number         |
| Room          | Room being booked             |
| Date          | Booking date                  |
| Start Time    | Booking start time            |
| End Time      | Booking finish time           |
| Price         | Total booking cost            |
| Status        | Pending, Approved or Rejected |

### Administrators

| Field            | Purpose                     |
| ---------------- | --------------------------- |
| Administrator ID | Unique administrator number |
| Username         | Login username              |
| Password         | Encrypted password          |
| Name             | Administrator name          |
