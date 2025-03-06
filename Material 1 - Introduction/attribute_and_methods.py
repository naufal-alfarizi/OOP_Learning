class Car:
    wheels = 4

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        a = f"{self.brand} {self.model} is Car."
        return a

my_car = Car("Toyota", "Corolla")
print(my_car.start())
