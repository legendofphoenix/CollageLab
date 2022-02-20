#Question 4
class Vehicle:
    def __init__(self, name, mileage,max_speed, capacity):
        self.name = name
        self.mileage = mileage
        self.max_speed = max_speed
        self.capacity = capacity
    def seating_capacity(self, capacity):
        print("The seating capacity of a",self.name,"is",capacity,"passengers")
class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)
School_bus = Bus("School Volvo", 180, 12,20)
print("Vehicle Name:", School_bus.name,"\nSpeed:", School_bus.max_speed)
print("\nMileage:", School_bus.mileage,"Capacity",School_bus.capacity)
print(School_bus.seating_capacity())
