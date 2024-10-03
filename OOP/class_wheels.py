from class_detail import Detail


class Wheel(Detail):

    in_need_spokes = True

    def __init__(self, name, wheel_width, price):
        super().__init__(name, price)
        self.wheel_width = wheel_width


    def get_name(self):
        return self.name, self.wheel_width, self.price, self.in_need_spokes


    def speak(self):
        return "Wheel " + self.name + " " + self.wheel_width + " " + self.price + " " + self.in_need_spokes
