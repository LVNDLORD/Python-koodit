# 2. Extend the program by adding an accerelate method into the new class.
# The method should receive the change of speed (km/h) as a parameter.
# If the change is negative, the car reduces speed.
# The method must change the value of the speed property of the object.
# The speed of the car must stay below the set maximum and cannot be less than zero.
# Extend the main program so that the speed of the car is first increased by +30 km/h,
# then +70 km/h and finally +50 km/h. Then print out the current speed of the car.

# Finally, use the emergency brake by forcing a -200 km/h change on the speed and then
# print out the final speed. The travelled distance does not have to be updated yet.

# Q&A
#  Extend the program by adding an accerelate method into the !!! new class !!?
class Car:
    reg_number = ''
    max_speed = 0
    current_speed = 0
    travelled_dist = 0

    def __init__(self, reg_num, max_speed, cur_speed, trav_dist):
        self.reg_number = reg_num
        self.max_speed = max_speed
        self.current_speed = cur_speed
        self.travelled_dist = trav_dist

    def accelerate(self, speed_change):
        self.current_speed += speed_change
        # print(f"{self.current_speed} current speed entry")
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0
        # print(f"{self.current_speed} current speed after eval")
        return self.current_speed


new_car = Car('ABC-123', 142, Car.current_speed, Car.travelled_dist)
print(new_car.__dict__)

print(new_car.accelerate(30))
print(new_car.accelerate(70))
print(new_car.accelerate(50))
print(new_car.current_speed) # 150 but 142
print(new_car.accelerate(-200)) # -58 but 0
print(new_car.current_speed) # 0 Final speed
print(new_car.__dict__)