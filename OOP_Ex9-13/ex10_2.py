
class Elevator:

    def __init__(self, bottom_floor, top_floor):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.cur_floor = bottom_floor

    def __str__(self):
        print(self.bottom_floor, self.top_floor, self.cur_floor)

    def floor_up(self):
        self.cur_floor += 1
        return self.cur_floor

    def floor_down(self):
        self.cur_floor -= 1
        return self.cur_floor

    def go_to_floor(self, floor):
        # print(f"Starting from floor num {self.cur_floor}")
        while self.cur_floor != floor:
            if self.cur_floor < floor:
                self.floor_up()
            else:
                self.floor_down()
        # print(f"Arrived to {self.cur_floor}")


class Buildings:

    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.num_elevators = num_elevators
        self.elevators_list = []
        for i in range(num_elevators):
            self.elevators_list.append(Elevator(self.bottom_floor, self.top_floor))

    def run_elevator(self, selected_el, destination):
        self.elevators_list[selected_el-1].go_to_floor(destination)
        # current position of all elevators
        # for i in self.elevators_list:
        #     print(i.__dict__)

    def fire_alarm(self):
        for el in self.elevators_list:
            if el.cur_floor == self.bottom_floor:
                continue
            el.go_to_floor(self.bottom_floor)
        # current position of all elevators
        # for i in self.elevators_list:
        #    print(i.__dict__)


if __name__ == '__main__':

    h = Elevator(1, 6)
    h.go_to_floor(5)
    h.go_to_floor(h.bottom_floor)

    build = Buildings(1, 6, 3)
    build.run_elevator(2, 5)
    build.fire_alarm()

