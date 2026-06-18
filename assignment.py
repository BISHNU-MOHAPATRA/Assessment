# Trip class to store ride details and calculate fare
class Trip:

    # Constructor to initialize trip details
    def __init__(self, distance, ride_type, is_peak_hour):
        self.__distance = distance
        self.__ride_type = ride_type
        self.__is_peak_hour = is_peak_hour

    # Getter method for distance
    def get_distance(self):
        return self.__distance

    # Getter method for ride type
    def get_ride_type(self):
        return self.__ride_type

    # Getter method for peak hour status
    def get_is_peak_hour(self):
        return self.__is_peak_hour

    # Method to calculate trip price
    def calculate_price(self):
        if self.__ride_type == "Standard":
            price = self.__distance * 1.50
        elif self.__ride_type == "Premium":
            price = self.__distance * 2.50
        else:
            price = 0

        # Add peak hour surcharge
        if self.__is_peak_hour:
            price += 5.00

        return price


# Create sample trip objects
trip1 = Trip(10.0, "Standard", True)
trip2 = Trip(5.5, "Premium", False)
trip3 = Trip(3.0, "Standard", False)

# Store trips in a list
trips = [trip1, trip2, trip3]

# Variables to store totals
total_distance = 0
total_fare = 0
total_points = 0

# Process all trips
for trip in trips:

    # Add distance
    total_distance += trip.get_distance()

    # Add fare
    total_fare += trip.calculate_price()

    # Calculate loyalty points
    if trip.get_ride_type() == "Premium":
        total_points += trip.get_distance() * 2
    else:
        total_points += trip.get_distance()

# Display final results
print("Total Distance Traveled:", total_distance)
print("Total Fare Due: $", format(total_fare, ".2f"))
print("Total Loyalty Points Earned:", total_points)# Trip class to store ride details and calculate fare
class Trip:

    # Constructor to initialize trip details
    def __init__(self, distance, ride_type, is_peak_hour):
        self.__distance = distance
        self.__ride_type = ride_type
        self.__is_peak_hour = is_peak_hour

    # Getter method for distance
    def get_distance(self):
        return self.__distance

    # Getter method for ride type
    def get_ride_type(self):
        return self.__ride_type

    # Getter method for peak hour status
    def get_is_peak_hour(self):
        return self.__is_peak_hour

    # Method to calculate trip price
    def calculate_price(self):
        if self.__ride_type == "Standard":
            price = self.__distance * 1.50
        elif self.__ride_type == "Premium":
            price = self.__distance * 2.50
        else:
            price = 0

        # Add peak hour surcharge
        if self.__is_peak_hour:
            price += 5.00

        return price


# Create sample trip objects
trip1 = Trip(10.0, "Standard", True)
trip2 = Trip(5.5, "Premium", False)
trip3 = Trip(3.0, "Standard", False)

# Store trips in a list
trips = [trip1, trip2, trip3]

# Variables to store totals
total_distance = 0
total_fare = 0
total_points = 0

# Process all trips
for trip in trips:

    # Add distance
    total_distance += trip.get_distance()

    # Add fare
    total_fare += trip.calculate_price()

    # Calculate loyalty points
    if trip.get_ride_type() == "Premium":
        total_points += trip.get_distance() * 2
    else:
        total_points += trip.get_distance()

# Display final results
print("Total Distance Traveled:", total_distance)
print("Total Fare Due: $", format(total_fare, ".2f"))
print("Total Loyalty Points Earned:", total_points)# Trip class to store ride details and calculate fare
class Trip:

    # Constructor to initialize trip details
    def __init__(self, distance, ride_type, is_peak_hour):
        self.__distance = distance
        self.__ride_type = ride_type
        self.__is_peak_hour = is_peak_hour

    # Getter method for distance
    def get_distance(self):
        return self.__distance

    # Getter method for ride type
    def get_ride_type(self):
        return self.__ride_type

    # Getter method for peak hour status
    def get_is_peak_hour(self):
        return self.__is_peak_hour

    # Method to calculate trip price
    def calculate_price(self):
        if self.__ride_type == "Standard":
            price = self.__distance * 1.50
        elif self.__ride_type == "Premium":
            price = self.__distance * 2.50
        else:
            price = 0

        # Add peak hour surcharge
        if self.__is_peak_hour:
            price += 5.00

        return price


# Create sample trip objects
trip1 = Trip(10.0, "Standard", True)
trip2 = Trip(5.5, "Premium", False)
trip3 = Trip(3.0, "Standard", False)

# Store trips in a list
trips = [trip1, trip2, trip3]

# Variables to store totals
total_distance = 0
total_fare = 0
total_points = 0

# Process all trips
for trip in trips:

    # Add distance
    total_distance += trip.get_distance()

    # Add fare
    total_fare += trip.calculate_price()

    # Calculate loyalty points
    if trip.get_ride_type() == "Premium":
        total_points += trip.get_distance() * 2
    else:
        total_points += trip.get_distance()

# Display final results
print("Total Distance Traveled:", total_distance)
print("Total Fare Due: $", format(total_fare, ".2f"))
print("Total Loyalty Points Earned:", total_points)