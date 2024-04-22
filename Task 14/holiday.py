print(f"Welcome to The Best Holidays booking system")

# Function to calculate hotel cost
def hotel_cost(num_nights):
    return num_nights * 100  # £100 per night

# Function to calculate plane cost
def plane_cost(city_flight):
    if city_flight == "New York":
        return 500
    elif city_flight == "London":
        return 600
    elif city_flight == "Accra":
        return 700
    else:
        return 400  # Default cost if they choose a city not on the list

# Function to calculate car rental cost
def car_rental(rental_days):
    return rental_days * 50  # £50 per day

# Function to calculate total holiday cost
def holiday_cost(city_flight, num_nights, rental_days):
    total_cost = hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)
    return total_cost

# Getting user inputs
city_flight = input("Enter the city you will be flying to (New York, London, Accra, etc.): ")
num_nights = int(input("Enter the number of nights you will be staying at a hotel: "))
rental_days = int(input("Enter the number of days for which you will be hiring a car: "))

# Calculating total holiday cost
total_cost = holiday_cost(city_flight, num_nights, rental_days)

# Printing details about the holiday
print("\nHoliday Details:")
print("City of Flight:", city_flight)
print("Number of Nights in Hotel:", num_nights)
print("Number of Days for Car Rental:", rental_days)
print("Total Cost of Holiday: £", total_cost)
