Airline Ticket Booking GUI
This is a simple airline ticket booking system built using Python's Tkinter library for the graphical user interface (GUI). It allows users to book adult and child tickets, calculates the total price, and keeps track of seat availability.

******Features******
Book Tickets: Users can book adult and child tickets.
Dynamic Pricing: Adult tickets are priced at £120 and child tickets at £60.
Seat Availability: The system starts with 152 available seats and updates the remaining seats after each booking.
Session Summary: Displays the number of tickets booked and total price for each session.
Final Summary: Shows a final summary of all tickets booked and the total price for the session.
Menu Options: Includes file, edit, format, run, options, and help menus, similar to common GUI applications.
Libraries Used
Tkinter: Used for building the GUI interface.
tkinter.messagebox: Used to show error messages when trying to overbook seats.
How to Use
Run the Script:

Make sure Python is installed.
Run the Python script using the following command:
bash
Copy code
python Airline-GUI_Tahmid\ Islam.py
Book Tickets:

Enter your forename and surname.
Input the number of adult and child tickets you want to book.
Click the Calculate button to see the price and remaining seats.
View Final Summary:

Click the Final Summary button to view the total tickets booked and total price for all sessions.
Clear the Session:

Click the Clear button to close the application.
Code Structure
Main Window: A Tkinter window is created with labels, entry fields, and buttons for user interaction.
Functions:
Cal(): Calculates the price for the current booking session and updates seat availability.
final(): Displays the final summary of tickets and total price.
Example Output
yaml
Copy code
✈Welcome to Tahmid Airlines✈
💸Price: Adult £120 Child £60
Session Summary:
Your Forename: John
Your Surname: Doe
Adult tickets booked: 2
Price for adult tickets booked: £240.00
Child tickets booked: 1
Price for child tickets booked: £60.00
Total price: £300.00
Seats left: 149
Course Information
Course: BTEC Level 3 Extended Diploma in IT
Unit: Programming
Term: Spring 2021
Contributing
Feel free to fork the repository, submit issues, and create pull requests for any improvements or new features.

License
This project is licensed under the MIT License.

