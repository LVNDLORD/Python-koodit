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


class ElectricCar(Car):

    def __init__(self, reg_num, max_speed, kw_h):
        self.kw_h = kw_h
        super().__init__(reg_num, max_speed)


class GasolineCar(Car):
    def __init__(self, reg_num, max_speed, liters):
        self.liters = liters
        super().__init__(reg_num, max_speed)


gas_car = GasolineCar("ACD-123", 165, 32.3)
el_car = ElectricCar("ABC-15", 180, 52.5)

gas_car.accelerate(100)
el_car.accelerate(100)

gas_car.drive(3)
el_car.drive(3)

print(gas_car.trav_dist)
print(el_car.trav_dist)

#ACD-123 165 100 300
#ABC-15 180 100 300
