# Testing Strategy

The BLBC Booking System will be tested throughout development to ensure it meets the functional and non-functional requirements.

The following types of testing will be carried out:

- Manual testing of all user functionality.
- Automatic testing of HTML and CSS
- Validation testing of all form inputs.
- Responsiveness testing on desktop, tablet and mobile devices.
- Browser compatibility testing.
- User acceptance testing to ensure the system meets user requirements.

Test results will be recorded during the development phase.

## Test Evidence

### HTML Validation
![HTML validation results](../assets/images/tests/html-validation.png)

### CSS Validation
![CSS validation results](../assets/images/tests/css-validation.png)

### Lighthouse
![Lighthouse results](../assets/images/tests/lighthouse.png)

### GitHub CI
![GitHub CI successful run](../assets/images/tests/github-ci-success.png)

### Home page
![Home page results](../assets/images/tests/home-page.png)

### Booking page
![Booking page](../assets/images/tests/booking-page.png)

### Availability page
![Availability page](../assets/images/tests/availability-page.png)

## Admin page
![Admin page](../assets/images/tests/admin-page.png)

### Manage My Bookings
![Manage My Bookings](../assets/images/tests/manage-bookings.png)

### Edit Booking
![Edit Booking](../assets/images/tests/edit-booking.png)

### Booking Updated
![Booking successfully updated](../assets/images/tests/booking-updated.png)

### Booking Deleted
![Booking successfully deleted](../assets/images/tests/booking-deleted.png)

### Mobile Home Page
![Mobile home page showing responsive navigation](../assets/images/tests/mobile-home-page.png)

## Manual Test Results

The following manual tests were carried out during development and on the deployed website.

| Test | Expected result | Outcome |
|---|---|---|
| Submit a booking with valid details | Booking request is accepted | Passed |
| Email verification | Verification code is sent and accepted | Passed |
| Submit a booking with missing required details | Validation prevents an incomplete booking | Passed |
| Attempt to double-book a room | Conflicting booking is prevented | Passed |
| Select a past booking time | Booking is rejected | Passed |
| Select an invalid time slot | Only half-hour intervals are permitted | Passed |
| Calculate the booking fee | Correct fee is calculated and displayed | Passed |
| View room availability | Availability is displayed correctly | Passed |
| View a booking in Django admin | Booking details are displayed correctly | Passed |
| Create a booking through the website | Booking is saved and displayed in Manage My Bookings | Passed |
| View a customer's bookings | The customer's booking details are displayed | Passed |
| Amend a booking through the website | Changes are saved and availability is updated | Passed |
| Delete a booking through the website | Booking is removed and the time slot becomes available | Passed |
| Edit or delete a booking through Django admin | Changes are saved or the booking is removed | Passed |
| Check booking amendment history | Website amendments are not recorded in Django admin history | Improvement identified |

The deployed website was tested on desktop, mobile phone and iPad in both portrait and landscape orientations. The tests confirmed that the pages displayed correctly and that the booking system's main functions worked as expected.

**Note:** The booking amendment history limitation is documented under Future Improvement.

### Future Improvement – Booking Amendment History

When a customer amends a booking through the website, the changes are saved correctly, but they are not recorded in Django admin's history log. Changes made directly through Django admin are recorded. A future enhancement could provide a history of customer booking amendments for easier tracking and auditing.

This does not prevent customers from amending their bookings, but it would improve administration and traceability.