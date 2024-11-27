# Base Class: Vehicle
class Vehicle:
    def move(self):
        print("This vehicle moves in its own way.")

# Subclass: Car
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Subclass: Plane
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Subclass: Boat
class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Example Usage
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    vehicle.move()
