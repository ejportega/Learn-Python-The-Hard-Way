cars  = 100 # total number of cars
space_in_a_car = 4 # car capacity
drivers = 30 # total drivers
passengers = 90 # total passengers
cars_not_driven = cars - drivers # cars not use
cars_driven = drivers # cars used
carpool_capacity = cars_driven * space_in_a_car # maximum oassenger
average_passengers_per_car = passengers / cars_driven #

print("There are", cars, "cars available.") # number of cars
print("There are only", drivers, "drivers available.") # number of drivers
print("There will be", cars_not_driven, "empty cars today.") # number cars that not had driven
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")


# Study Drills
'''
    1. The answer will not in floating point number
'''
