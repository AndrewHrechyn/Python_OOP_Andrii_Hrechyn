from class_user import User
from class_employee import Employee
from class_detail import Detail
from class_frame import Frame
#from class_wheels import Wheels


class OneLegFork(Detail):

    leg_size = 1

    def __init__(self, name, length, year, width, material, price):
        super().__init__(name, price)
        self.length = length
        self.year = year
        self.width = width
        self.material = material

    def get_info(self):
        return f"One-Leg Fork: {self.name}, Leg Size: {self.leg_size}, {super().get_info()}"

    def speak(self):
        return f"{self.name} says: I'm a one-leg fork!"


class TwoLegFork(Detail):

    leg_size = 2

    def __init__(self, name, length, year, width, material, price):
        super().__init__(name, price)
        self.length = length
        self.year = year
        self.width = width
        self.material = material

    def get_info(self):
        return f"Two-Leg Fork: {self.name}, Leg Size: {self.leg_size}, {super().get_info()}"

    def speak(self):
        return f"{self.name} says: I'm a two-leg fork!"


class Fork(OneLegFork, TwoLegFork):
    def speak(self):
        return f"{self.name} says: I'm a fork!"



user = User("Alice", 25, "alice@example.com", "password123", "2023-09-01")

if User.validate(user.email):
    print(f"Valid email: {user.email}")
else:
    print(f"Invalid email: {user.email}")

user = User("Alice", 25, "alice@example.com", "password123", "2023-09-01")

if User.validate(user.email):
    print(f"Valid email: {user.email}")
else:
    print(f"Invalid email: {user.email}")

frame = Frame("Trek Frame", "M", "Aluminum", 2022, 500, full_suspension=True)
one_leg_fork = OneLegFork("OneLeg Fork", 120, 2021, 15, "Carbon", price=300)
two_leg_fork = TwoLegFork("Rockshox", 160, 2023, 15, "Carbon", price=600)

user.add_detail(frame)
user.add_detail(one_leg_fork)
user.add_detail(two_leg_fork)

print("\nDetails added to the user:")
for detail in user.get_details():
    print(detail)

print("\nCheckout process:")
user.checkout()

print("\nChanging password:")
user.change_password(user.get_pincode, "new_secure_password")

print("\nUser information:")
print(user.get_info())

print("\nSpeak demonstration:")
print(user.speak())
print(frame.speak())
print(one_leg_fork.speak())
print(two_leg_fork.speak())

employee = Employee("Bob", 30, "bob@example.com", "emp123")
print("\nEmployee processing orders:")
employee.process_order()
employee.process_order()

print("\nEmployee information:")
print(employee.get_info())

print("\nWarranty information for TwoLeg Fork with warranty:")
print(two_leg_fork.get_info())
