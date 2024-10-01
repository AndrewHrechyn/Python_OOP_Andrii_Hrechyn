from random import randint
from class_creature import Creature

class User(Creature):

    def __init__(self, name, age, email, password, created_at):
        super().__init__(name, age)
        self.email = email
        self.__password = password
        self.created_at = created_at
        self.__pincode = randint(100, 1000)
        self.details = []
        print("Your account has been created")
        print("It`s your private pincode: " + str(self.__pincode))

    @staticmethod
    def validate(email):
        if "@" in email and "." in email:
            return True
        return False

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Email: {self.email}, Created at: {self.created_at}"

    @property
    def get_pincode(self):
        return self.__pincode

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_password):
        self.__password = new_password

    def change_password(self, pincode, new_password):
        if pincode == self.__pincode:
            self.password = new_password
            print(f"Password changed successfully")
        else:
            print("Failed to change password")

    def add_detail(self, detail):
        self.details.append(detail)
        print(f"{detail.name} added to {self.name}'s bike details.")

    def get_details(self):
        return [detail.get_info() for detail in self.details]

    def checkout(self):
        if not self.details:
            print("No items in the cart to checkout.")
            return
        print("Generating checkout receipt...")
        total = 0
        for detail in self.details:
            print(detail.get_info())
            total += detail.price
        print(f"Total Price: {total} USD")
        print("Thank you for your purchase!")

    def speak(self):
        return f"{self.name} says: I'm a user!"
