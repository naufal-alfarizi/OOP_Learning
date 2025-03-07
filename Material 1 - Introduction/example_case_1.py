import pandas as pd

class Car:
    def __init__(self, brand, model, year, price, availability):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        self.__availability = availability

    def is_available(self):
        return self.__availability == "Available"

    def mark_sold(self):
        if self.is_available():
            self.__availability = "Sold"
            print(f"{self.brand} {self.model} has been sold.")
        else:
            print(f"{self.brand} {self.model} is already sold.")

    def display(self):
        availability = "Available" if self.is_available() else "Sold"
        print(f"{self.year} {self.brand} {self.model} - ${self.price} [{availability}]")

class Showroom:
    def __init__(self, name):
        self.name = name
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def load_cars_from_csv(self, filename):
        df = pd.read_csv(filename)
        for _, row in df.iterrows():
            car = Car(row['brand'], row['model'], row['year'], row['price'], row['availability'])
            self.add_car(car)

    def show_all_cars(self):
        print(f"\nCars in {self.name} Showroom:")
        for car in self.cars:
            car.display()

    def show_available_cars(self):
        print(f"\nAvailable Cars in {self.name} Showroom:")
        for car in self.cars:
            if car.is_available():
                car.display()

    def sell_car(self, brand, model):
        for car in self.cars:
            if car.brand == brand and car.model == model:
                car.mark_sold()
                return
        print(f"No {brand} {model} found in the showroom.")


showroom = Showroom("Elite Cars")
showroom.load_cars_from_csv("cars.csv")

showroom.show_all_cars()
showroom.show_available_cars()
showroom.sell_car("Toyota", "Agya")
showroom.show_available_cars()
