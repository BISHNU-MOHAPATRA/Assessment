# Assessment
Ride-Share Trip & Loyalty Calculator

Overview
This project implements a Ride-Share Trip & Loyalty Calculator using Object-Oriented Programming (OOP) in Python.

The system calculates:
* Total trip fare based on ride type and peak-hour charges.
* Total loyalty points earned by the passenger.

Features
* Encapsulation using private attributes.
* Constructor for initializing trip details.
* Getter methods for accessing trip information.
* Fare calculation for Standard and Premium rides.
* Peak-hour surcharge support.
* Loyalty points calculation.
* Processing multiple trips using loops.

Ride Pricing Rules
* Standard Ride: $1.50 per unit distance
* Premium Ride: $2.50 per unit distance
* Peak Hour Surcharge: $5.00

Loyalty Points Rules
* Standard Ride: 1 point per unit distance
* Premium Ride: 2 points per unit distance

Sample Input
Trip 1: Distance = 10.0, Ride Type = Standard, Peak Hour = True
Trip 2: Distance = 5.5, Ride Type = Premium, Peak Hour = False
Trip 3: Distance = 3.0, Ride Type = Standard, Peak Hour = False

Expected Output
Total Distance Traveled: 18.5
Total Fare Due: $38.25
Total Loyalty Points Earned: 24.0
