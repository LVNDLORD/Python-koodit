import random


class Car:

    def __init__(self, reg_num, max_speed, cur_speed=0, trav_dist=0):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.cur_speed = cur_speed
        self.trav_dist = trav_dist

    def __str__(self):
        print(self.reg_num, self.max_speed, self.cur_speed, self.trav_dist)

    def accelerate(self, cur_speed):
        self.cur_speed += cur_speed
        if self.cur_speed > self.max_speed:
            self.cur_speed = self.max_speed
        elif self.cur_speed < 0:
            self.cur_speed = 0
        return self.cur_speed

    def drive(self, time):
        driven_per_time = self.cur_speed * time
        self.trav_dist += driven_per_time
        return self.trav_dist


if __name__ == '__main__':

    racing = True
    hours_race = 0
    race_dist = 10000
    car_list = []

    for i in range(10):
        car_list.append(Car(f"ABC-{i + 1}", random.randint(100, 200)))

    while racing:
        hours_race += 1
        for car in car_list:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)
            if car.trav_dist >= race_dist:
                print(f"Race lasted for {hours_race} hours. "
                      f"The winner who first reached {race_dist}km is {car.reg_num}!")
                racing = False
                break

    for each_car in car_list:
        each_car.__str__()

