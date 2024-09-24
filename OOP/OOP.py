from random import randint


class Creature:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}"

    def speak(self):
        return "I am a creature"


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


class Detail:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_info(self):
        return f"Detail: {self.name}, Price: {self.price} USD"

    def speak(self):
        return f"{self.name} says: I am a detail!"


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


class Fork(Detail):

    def __init__(self, name, length, year, width, material, price):
        super().__init__(name, price)
        self.length = length
        self.year = year
        self.width = width
        self.material = material

    def get_info(self):
        return f"Fork: {self.name}, Length: {self.length}, Width: {self.width}, Material: {self.material}, Year: {self.year}, Price: {self.price} USD"

    def speak(self):
        return f"{self.name} says: I'm a fork!"


class OneLegFork(Fork):
    def __init__(self, name, length, year, width, material, leg_size, price):
        super().__init__(name, length, year, width, material, price)
        self.leg_size = leg_size

    def get_info(self):
        return f"One-Leg Fork: {self.name}, Leg Size: {self.leg_size}, {super().get_info()}"

    def speak(self):
        return f"{self.name} says: I'm a one-leg fork!"


class TwoLegFork(Fork):
    def __init__(self, name, length, year, width, material, leg_size, price):
        super().__init__(name, length, year, width, material, price)
        self.leg_size = leg_size

    def get_info(self):
        return f"Two-Leg Fork: {self.name}, Leg Size: {self.leg_size}, {super().get_info()}"

    def speak(self):
        return f"{self.name} says: I'm a two-leg fork!"


class Warranty:
    def __init__(self, warranty_years):
        self.warranty_years = warranty_years

    def get_warranty_info(self):
        return f"Warranty: {self.warranty_years} years"


class OneLegForkWithWarranty(OneLegFork, Warranty):
    def __init__(self, name, length, year, width, material, leg_size, warranty_years, price):
        OneLegFork.__init__(self, name, length, year, width, material, leg_size, price)
        Warranty.__init__(self, warranty_years)

    def get_full_info(self):
        return f"{self.get_info()}, {self.get_warranty_info()}"

    def speak(self):
        return f"{self.name} says: I'm a one-leg fork with a warranty!"


class TwoLegsWithWarranty(TwoLegFork, Warranty):
    def __init__(self, name, length, year, width, material, leg_size, warranty_years, price):
        TwoLegFork.__init__(self, name, length, year, width, material, leg_size, price)
        Warranty.__init__(self, warranty_years)

    def get_full_info(self):
        return f"{self.get_info()}, {self.get_warranty_info()}"

    def speak(self):
        return f"{self.name} says: I'm a two-leg fork with a warranty!"


user = User("Alice", 25, "alice@example.com", "password123", "2023-09-01")

if User.validate(user.email):
    print(f"Valid email: {user.email}")
else:
    print(f"Invalid email: {user.email}")

frame = Frame("Trek Frame", "M", "Aluminum", 2022, 500, full_suspension=True)
one_leg_fork = OneLegFork("OneLeg Fork", 120, 2021, 15, "Carbon", leg_size=40, price=300)
two_leg_fork_with_warranty = TwoLegsWithWarranty("TwoLeg Fork", 130, 2022, 16, "Steel", leg_size=45, warranty_years=3, price=400)

user.add_detail(frame)
user.add_detail(one_leg_fork)
user.add_detail(two_leg_fork_with_warranty)

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
print(two_leg_fork_with_warranty.speak())

employee = Employee("Bob", 30, "bob@example.com", "emp123")
print("\nEmployee processing orders:")
employee.process_order()
employee.process_order()

print("\nEmployee information:")
print(employee.get_info())

print("\nWarranty information for TwoLeg Fork with warranty:")
print(two_leg_fork_with_warranty.get_full_info())
