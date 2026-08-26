class Car:
    brand = None
    model = None
    colour = None
    def __init__(self, car_colour):
        self.colour = car_colour

    def car_name(self):
        print(f"{self.brand} {self.model}")

my_car = Car(car_colour="Red")
my_car.brand = "Audi"
my_car.model = "RS 8"

print(my_car)
print(my_car.brand)
print(my_car.model)
print(my_car.colour)
my_car.car_name()

#INHERITANCE
class ElectricCar(Car):
    def __init__(self, battery_size, brand, model, colour):
        self.battery_size = battery_size
        super().__init__(car_colour=colour)
        self.brand = brand
        self.model = model
    def carBatterySizeAndColour(self):
        return f"{self.battery_size} {self.colour}"


my_e_car = ElectricCar(battery_size=12, brand= "Tata", model="sierra", colour="white")
my_e_car.car_name()
print(my_e_car.carBatterySizeAndColour())

#ENCAPSULATION
class CNGCar(Car):
    __capacity = None
    def __init__(self, brand, model, colour):
        super().__init__(car_colour=colour)
        self.brand = brand
        self.model = model
    def setCapacity(self, capacity):
        self.__capacity = capacity
    def getCapacity(self):
        return self.__capacity

cng_car = CNGCar(brand="SUZUKI", model="swift", colour="Cherry red")
cng_car.setCapacity(20)

print(cng_car.getCapacity())
