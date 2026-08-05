# User Stories

User stories describe the main functionality of the BLBC Booking System from the perspective of its users. Each user story will later be converted into a GitHub issue with acceptance criteria and development tasks.

---

# Visitor User Stories

## US1 - View available rooms

**As a visitor, I want to view available rooms, so that I can choose a suitable room for my needs.**

### Acceptance Criteria

* Rooms available for hire are displayed.
* Room descriptions are shown.
* Room capacities are shown.
* Room photographs are displayed.

---

## US2 - Check room availability

**As a visitor, I want to check room availability, so that I know whether my chosen date and time is available.**

### Acceptance Criteria

* Available dates can be viewed.
* Existing bookings are considered.
* Visitors cannot request unavailable time slots.

---

## US3 - Submit booking request

**As a visitor, I want to submit a booking request, so that I can request to hire a room.**

### Acceptance Criteria

* Required information must be completed.
* Booking details are stored.
* New bookings are given a Pending status.

---

## US4 - Verify email address

**As a visitor, I want to verify my email address, so that my identity can be confirmed before submitting a booking request.**

### Acceptance Criteria

* A verification code is sent to the visitor's email address.
* The visitor can enter the verification code.
* A booking request cannot be submitted without successful verification.

---

## US5 - View booking terms and conditions

**As a visitor, I want to view booking terms and conditions, so that I understand the requirements before submitting a booking request.**

### Acceptance Criteria

* Terms and conditions are available before submission.
* Visitors can review the requirements for hiring rooms.

---

# Administrator User Stories

## US6 - Administrator login

**As an administrator, I want to log in securely, so that only authorised users can manage bookings.**

### Acceptance Criteria

* Administrators must provide valid login details.
* Unauthorised users cannot access administration features.

---

## US7 - Review booking requests

**As an administrator, I want to view booking requests, so that I can decide whether they should be approved.**

### Acceptance Criteria

* Pending bookings are displayed.
* Booking details are available.

---

## US8 - Approve booking requests

**As an administrator, I want to approve booking requests, so that confirmed bookings are recorded.**

### Acceptance Criteria

* Administrators can approve pending bookings.
* Approved bookings are updated with the correct status.

---

## US9 - Reject booking requests

**As an administrator, I want to reject booking requests, so that unsuitable bookings are not accepted.**

### Acceptance Criteria

* Administrators can reject pending bookings.
* Rejected bookings are updated with the correct status.

---

## US10 - Manage rooms

**As an administrator, I want to manage room information, so that visitors see accurate room details.**

### Acceptance Criteria

* Administrators can add rooms.
* Administrators can edit room details.
* Administrators can temporarily disable rooms.

---

# System User Stories

## US11 - Store booking information

**As the system, I want to store booking information, so that bookings can be managed correctly.**

### Acceptance Criteria

* Booking information is stored securely.
* Each booking has a unique reference.
* Bookings are linked to rooms and customers.

---

## US12 - Prevent double bookings

**As the system, I want to prevent double bookings, so that the same room cannot be booked more than once at the same time.**

### Acceptance Criteria

* Existing bookings are checked before accepting requests.
* Conflicting bookings are prevented.

---

## US13 - Send booking emails

**As the system, I want to send booking emails, so that visitors and administrators receive important booking updates.**

### Acceptance Criteria

* Visitors receive booking acknowledgement emails.
* Administrators can be notified of new booking requests.
