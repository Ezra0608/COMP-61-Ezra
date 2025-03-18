class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_car_info(self):
        return f"{self.year} {self.make} {self.model}"

pass
pass

class Owner:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.cars_owned = []
    
    def purchase_car(self, car):
        if isinstance(car, Car):  
            self.cars_owned.append(car)
            print(f"{self.name} just purchased a {car.get_car_info()}.")
        else:
            print("Invalid input: Only Car objects can be added.")

    def show_owned_cars(self):
        if not self.cars_owned:
            print(f"{self.name} does not own any cars.")
        else:
            print(f"{self.name} owns the following cars:")
            for car in self.cars_owned:
                print(f" - {car.get_car_info()}")
        pass

def main():
    car1 = Car("Toyota", "Tacoma", 2011)
    car2 = Car("Honda", "Pilot", 2017)
    car3 = Car("Kia", "Telluride", 2022)
    car4 = Car("Volkswagen", "Beetle", 1966)
    car5 = Car("Porsche", "Cayanne", 2021)
    car6 = Car("Mazda", "Miata", 2014)

    owner1 = Owner("Steve", 48)
    owner2 = Owner("Kelly", 46)
    owner3 = Owner("Michael", 45)

    owner1.purchase_car(car1)
    owner1.purchase_car(car6)

    owner2.purchase_car(car3)
    owner2.purchase_car(car2)

    owner3.purchase_car(car4)
    owner3.purchase_car(car5)

    owner1.show_owned_cars()
    owner2.show_owned_cars()
    owner3.show_owned_cars()

if __name__ == "__main__":
    main()