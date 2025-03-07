class Car:
    def set_details(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.board} {self.model}")

# Creating an object of Car
car1 = Car()
car1.set_details("Toyota", "Camry", 2022)  # Manually setting attributes
car1.display_info()  # Output: 2022 Toyota Camry
