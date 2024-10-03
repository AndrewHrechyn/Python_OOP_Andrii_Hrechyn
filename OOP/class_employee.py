from random import randint
from class_creature import  Creature

class Employee(Creature):

    def __init__(self, name, age, email, password):
        super().__init__(name, age)
        self.email = email
        self.__password = password
        self.__pincode = randint(100, 1000)
        self.orders_processed = 0
        print("Your account has been created")

    def process_order(self):
        self.orders_processed += 1
        print(f"Order processed. Total processed: {self.orders_processed}")

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Email: {self.email}, Orders processed: {self.orders_processed}"

    def speak(self):
        return f"{self.name} says: I'm an employee!"