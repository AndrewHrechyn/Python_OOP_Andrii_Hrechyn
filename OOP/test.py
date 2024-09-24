class Car:

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def is_driving(self):
        print("This" + self.model + "is driving")

    def stop(self):
        print("This" + self.model + "is stopping")






car_1 = Car("Ford", "Ford", 2020, "Black")
car_1.is_driving()
car_1.stop()

car_2 = Car("Ford", "Mustang", 1986, "Red")
car_2.is_driving()
car_2.stop()