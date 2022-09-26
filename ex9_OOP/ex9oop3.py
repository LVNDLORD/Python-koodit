# Again, extend the program by adding a new drive method that receives the number of hours as a parameter.
# The method increases the travelled distance by how much the car has travelled in constant speed in the given time.

# Example: The travelled distance of car object is 2000 km. The current speed is 60 km/h.
# Method call car.drive(1.5) increases the travelled distance to 2090 km.

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
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0
        return self.current_speed

    def drive(self, time_in_hours):
        self.travelled_dist = self.current_speed * time_in_hours
        return self.travelled_dist


new_car = Car('ABC-123', 142, Car.current_speed, Car.travelled_dist)
print(new_car.__dict__)

# print(new_car.accelerate(30))
# print(new_car.accelerate(70))
# print(new_car.accelerate(50))
# print(new_car.current_speed) # 150 but 142
# print(new_car.accelerate(-200)) # -58 but 0
# print(new_car.current_speed) # 0 Final speed
# print(new_car.__dict__)

print(new_car.accelerate(60))
print(new_car.drive(1.5))
print(new_car.__dict__)