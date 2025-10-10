# Vehicle Class Example

class Vehicle:
    def __init__(self, brand, model, speed):
        self.brand = brand
        self.model = model
        self.speed = speed  # in km/h

    def start(self):
        print(f"{self.brand} {self.model} is starting...")

    def accelerate(self, increase):
        self.speed += increase
        print(f"{self.brand} {self.model} accelerated. New speed: {self.speed} km/h")

    def brake(self, decrease):
        if self.speed - decrease >= 0:
            self.speed -= decrease
        else:
            self.speed = 0
        print(f"{self.brand} {self.model} slowed down. Current speed: {self.speed} km/h")

    def display_info(self):
        print(f"🚘 Vehicle Info:\nBrand: {self.brand}\nModel: {self.model}\nSpeed: {self.speed} km/h")


# Example usage
car = Vehicle("Toyota", "Innova", 60)
car.display_info()
car.start()
car.accelerate(40)
car.brake(30)
car.display_info()
