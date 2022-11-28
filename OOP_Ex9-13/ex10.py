
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
        while self.cur_floor != floor:
            self.__str__()
            if self.cur_floor < floor:
                self.floor_up()
            else:
                self.floor_down()


if __name__ == '__main__':

    h = Elevator(1, 6)
    h.go_to_floor(5)
    h.go_to_floor(h.bottom_floor)
    h.__str__()
