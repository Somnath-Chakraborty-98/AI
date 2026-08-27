class Car:
    brand = None
    model = None
    colour = None
    def __init__(self, car_colour):
        self.colour = car_colour

    def car_name(self):
        print(f"{self.brand} {self.model}")

    def fuel_type(self):
        return "Petrol"

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

    def fuel_type(self):
            return "Electric"


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

    def fuel_type(self):
            return "CNG"

cng_car = CNGCar(brand="SUZUKI", model="swift", colour="Cherry red")
cng_car.setCapacity(20)

print(cng_car.getCapacity())

#POLYMORPHISM

print(my_car.fuel_type())
print(my_e_car.fuel_type())
print(cng_car.fuel_type())


class Bike:
    __brand = None
    __model = None
    __colour = None

    total_count = 0

    def __init__(self, brand, model, colour):
        self.__brand = brand
        self.__model = model
        self.__colour = colour
        Bike.total_count += 1

    def get_bike_details(self):
        return f"{self.__brand} {self.__model} {self.__colour}"

    def get_total_bikes_created(self):
        return f"{self.total_count}"

    @staticmethod
    def bike_power():
        return "More than 40BHP"

    @property
    def model(self):
        return f"{self.__model}"

my_bike_1 = Bike(brand="KTM", model="Duke 390", colour="Black")
my_bike_2 = Bike(brand="Royal Enfeild", model="Himalayan 450", colour="Mana Black")

print(my_bike_1.get_bike_details())
print(my_bike_2.get_bike_details())
print(my_bike_1.get_total_bikes_created())

my_bike_3 = Bike(brand="Triumph", model="Street Triple RS", colour="Red")
print(my_bike_3.get_bike_details())
print(Bike.total_count)

#static
print(my_bike_1.bike_power())
print(Bike.bike_power())

#decoraters
print(my_bike_1.model)

print(isinstance(my_bike_1, Bike))

#Multiple Inheritance
class power:
    def bhp(self):
        return "More than 100BHP"

class torque:
    def nm(self):
        return "More than 100NM"

class SuperBike(power, torque, Bike):
    pass

my_bike_4 = SuperBike(brand="BMW", model="S100RR", colour="White")
print(my_bike_4.bhp())
print(my_bike_4.nm())