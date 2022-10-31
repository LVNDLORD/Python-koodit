
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
        print(f"Starting from floor num {self.cur_floor}")
        while self.cur_floor != floor:
            print(f"Currently at floor num {self.cur_floor}")
            #self.__str__()
            if self.cur_floor < floor:
                self.floor_up()
            else:
                self.floor_down()
        print(f"Arrived to {self.cur_floor}")


class Buildings:

    def __init__(self, bottom_floor, top_floor, num_elevators=0):
        # self.top_floor = top_floor
        # self.bottom_floor = bottom_floor
        self.num_elevators = num_elevators
        elevators_list = list(range(1, num_elevators + 1))  # 1 2 3 4

    def run_elevator(self, selected_el, destination):

        self.destination = destination


if __name__ == '__main__':

    h = Elevator(1, 6)
    h.go_to_floor(5)
    h.go_to_floor(h.bottom_floor)
    h.__str__()