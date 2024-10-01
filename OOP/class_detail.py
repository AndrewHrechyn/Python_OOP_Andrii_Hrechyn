class Detail:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_info(self):
        return f"Detail: {self.name}, Price: {self.price} USD"

    def speak(self):
        return f"{self.name} says: I am a detail!"