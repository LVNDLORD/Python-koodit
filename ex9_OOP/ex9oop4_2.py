# Now we will program a car race. The travelled distance of a new car is initialized as zero.
# At the beginning of the main program, create a list that consists of 10 car objects created using a loop.
# The maximum speed of each new car is a random value between 100 km/h and 200 km/h.
# The registration numbers are created as follows: "ABC-1", "ABC-2" and so on. Now the race begins.
# Done

# One per every hour of the race, the following operations are performed:
#
# The speed of each car is changed so that the change in speed is a random value between -10 km/h and +15 km/h.
# This is done using the accerelate method.
# Each car is made to drive for one hour. This is done with the drive method.
# The race continues until one of the cars has advanced at least 10,000 kilometers.
# Finally, the properties of each car are printed out formatted into a clear table.


# Q&A
import random

car_list = [None] * 10
for i in range(len(car_list)):
    new_racecar = []
    new_racecar.insert(0, f"ABC-{i + 1}")
    new_racecar.insert(1, random.randint(100, 200))
    car_list.pop(0)
    car_list.append(new_racecar)
    # print(car_list)
    # [['ABC-1', 115], ['ABC-2', 176], ['ABC-3', 118], ['ABC-4', 129], ['ABC-5', 124], ['ABC-6', 143], ['ABC-7', 144], ['ABC-8', 170], ['ABC-9', 116], ['ABC-10', 116]]


# new_car = Car('ABC-123', 142, Car.current_speed, Car.travelled_dist)


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
        self.drive(self.accelerate(random.randint(-10, 15)))
        # print(self.reg_number, self.max_speed, self.current_speed, self.travelled_dist)

    def accelerate(self, current_speed):
        self.current_speed += current_speed
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0
        return self.current_speed

    def drive(self, time_in_hours):
        self.travelled_dist = self.current_speed * time_in_hours
        # print(str(time_in_hours) + "time")
        # print(self.travelled_dist, "traveled" )
        return self.travelled_dist




# for i in car_list:  # adding all 10 cars from a list to a class as separate objects
#     Car(i[0], i[1], Car.current_speed, Car.travelled_dist)
empty = []
for i in car_list:
    empty.append(Car(i[0], i[1], Car.current_speed, Car.travelled_dist))

for i in empty:
    print(i.__dict__)



# One per every hour of the race, the following operations are performed:
#
# The speed of each car is changed so that the change in speed is a random value between -10 km/h and +15 km/h.
# This is done using the accerelate method.
# Each car is made to drive for one hour. This is done with the drive method.
# The race continues until one of the cars has advanced at least 10,000 kilometers.
# Finally, the properties of each car are printed out formatted into a clear table.


# print(Car.__dict__)


# print(new_car.__dict__)

# print(new_car.accelerate(30))
# print(new_car.accelerate(70))
# print(new_car.accelerate(50))
# print(new_car.current_speed) # 150 but 142
# print(new_car.accelerate(-200)) # -58 but 0
# print(new_car.current_speed) # 0 Final speed
# print(new_car.__dict__)

# print(new_car.accelerate(60))
# print(new_car.drive(1.5))
# print(new_car.__dict__)
