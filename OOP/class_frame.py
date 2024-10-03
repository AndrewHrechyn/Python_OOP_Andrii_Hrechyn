from class_detail import Detail

class Frame(Detail):

    def __init__(self, name, size, material, year, price, full_suspension=False):
        super().__init__(name, price)
        self.size = size
        self.material = material
        self.year = year
        self.full_suspension = full_suspension

    def get_info(self):
        suspension = "Yes" if self.full_suspension else "No"
        return f"Frame: {self.name}, Size: {self.size}, Material: {self.material}, Year: {self.year}, Full Suspension: {suspension}, Price: {self.price} USD"

    def speak(self):
        return f"{self.name} says: I'm a frame!"