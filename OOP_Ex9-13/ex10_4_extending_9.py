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


class Race:

    def __init__(self, name, distance_km, cars: list):
        self.name = name
        self.cars = cars
        self.distance_km = distance_km
        self.winner = ''
        self.hours_race = 0

    def hours_passes(self):
        for each_car in car_list:
            each_car.accelerate(random.randint(-10, 15))
            each_car.drive(1)
            self.race_finished()

    def print_status(self):
        for each_car in self.cars:
            each_car.__str__()

    def race_finished(self):
        for each_car in self.cars:
            if each_car.trav_dist >= self.distance_km:
                self.winner = each_car.reg_num
                return True


if __name__ == '__main__':

    car_list = []
    for i in range(10):
        car_list.append(Car(f"ABC-{i + 1}", random.randint(100, 200)))

    race = Race("Grand Demolition Derby", 8000, car_list)

    while not race.race_finished():
        race.hours_race += 1
        if race.hours_race % 10 == 0:
            print()
            print(f"{race.hours_race} hours of race passed")
            print()
            race.print_status()
        else:
            race.hours_passes()

    print(f"\nRace {race.name} lasted for {race.hours_race} h. The winner is {race.winner}!")
    race.print_status()
