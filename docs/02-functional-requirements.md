## 1. Visitor Requirements

| ID    | Requirement                                                                           | Priority               |
| ----- | ------------------------------------------------------------------------------------- | ---------------------- |
| FR1.1 | The system shall display all rooms available for hire. | Must
| FR1.2 | The system shall display room descriptions, capacities and photographs. | Must
| FR1.3 | The system shall allow visitors to check room availability. | Must
| FR1.4 | The system shall allow visitors to submit a booking request. | Must
| FR1.5 | The system shall validate mandatory fields before submission. | Must
| FR1.6 | The system shall display a confirmation message when a booking request is submitted. | Must
| FR1.7 | The system shall send a verification code to the visitor's email address. | Must                   |
| FR1.8 | The system shall require the visitor to enter the verification code before a booking request can be submitted.                     | Must                   |
| FR1.9 | The system shall reject booking requests where the email address has not been verified. | Must
| FR1.10 | The system shall allow visitors to view booking terms and conditions before submitting a booking request. | Must


## 2. Booking Requirements

| ID    | Requirement                                                                           | Priority               |
| ----- | ------------------------------------------------------------------------------------- | ---------------------- |
| FR2.1 | The system shall store all booking requests in the database. | Must
| FR2.2 | The system shall assign a status of Pending to new bookings. | Must
| FR2.3 | The system shall prevent double bookings. | Must
| FR2.4 | The system shall record the booking date and time. | Must
| FR2.5 | The system shall associate each booking with a room and customer. | Must
| FR2.6 | The system shall generate a unique booking reference. | Must
| FR2.7 | The system shall send a booking acknowledgement email after a booking request has been submitted. | Must

## 3. Administrator Requirements

| ID    | Requirement                                                                           | Priority               |
| ----- | ------------------------------------------------------------------------------------- | ---------------------- |
| FR3.1 | The system shall require administrators to log in. | Must
| FR3.2 | The system shall display all pending bookings. | Must
| FR3.3 | The system shall allow administrators to approve bookings. | Must
| FR3.4 | The system shall allow administrators to reject bookings. | Must
| FR3.5 | The system shall allow administrators to edit bookings. | Must
| FR3.6 | The system shall allow administrators to cancel bookings. | Must
| FR3.7 | The system shall allow administrators to search bookings. | Should
| FR3.8 | The system shall display booking history. | Should

## 4. Room Management

| ID    | Requirement                                                                           | Priority               |
| ----- | ------------------------------------------------------------------------------------- | ---------------------- |
|FR4.1 | The system shall allow administrators to add new rooms. | Must
|FR4.2 | The system shall allow administrators to edit room information. | Must
|FR4.3 | The system shall allow administrators to temporarily disable a room from accepting bookings. | Must
|FR4.4 | The system shall store room capacities and hire charges. | Must
|FR4.5 | The system shall allow administrators to upload room photographs. | Must

## 5. Security

| ID    | Requirement                                                                           | Priority               |
| ----- | ------------------------------------------------------------------------------------- | ---------------------- |
|FR5.1 | The system shall authenticate administrator accounts. | Must
|FR5.2 | The system shall prevent unauthorised access to the administration area. | Must
|FR5.3 | The system shall validate all user input. | Must
|FR5.4 | The system shall protect stored booking data. | Must
| FR5.5 | The system shall support SMS verification in a future release.                        | Won't (Future Release) |
| FR5.6 | The system shall expire email verification codes after a specified time. | Must

## 6. Reporting

| ID    | Requirement                                                                           | Priority               |
| ----- | ------------------------------------------------------------------------------------- | ---------------------- |
| FR6.1 | The system shall display today's bookings. | Should
| FR6.2 | The system shall display upcoming bookings. | Should
| FR6.3 | The system shall display booking statistics. | Could