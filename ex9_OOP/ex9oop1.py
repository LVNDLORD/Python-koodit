# 1. Write a Car class that has the following properties: registration number,
# maximum speed, current speed and travelled distance.
#
# Add a class initializer that sets the first two of the properties based on parameter values.
# The current speed and travelled distance of a new car must be automatically set to zero.

# Write a main program where you create a new car (registration number ABC-123,
# maximum speed 142 km/h). Finally, print out all the properties of the new car.

# Q&A
# max speed as int or string?
# "class that has the following properties?" Maybe attributes. Class variables?
# The current speed and travelled distance of a new car must be automatically set to zero?

class Car:
    reg_number = ''
    max_speed = ''
    current_speed = 0
    travelled_dist = 0

    def __init__(self, reg_num, max_speed, cur_speed, trav_dist):
        self.reg_number = reg_num
        self.max_speed = str(max_speed) + " km/h"
        self.current_speed = cur_speed
        self.travelled_dist = trav_dist


new_car = Car('ABC-123', 142, Car.current_speed, Car.travelled_dist)
print(new_car.__dict__)



