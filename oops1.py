class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")

    
# this is our object 1
# Creating an object of Car
car1 = Car("Toyota", "Camry", 2022)






# we are checking or watching our created object
# Output: 2022 Toyota Camry
car1.display_info()  # Output: 2022 Toyota Camry





# this is our object 2
# Creating another object of Car
car2 = Car("Honda", "Accord", 2023)






# we are checking or watching our created object 2
# Output: 2023 Honda Accord 
car2.display_info()  # Output: 2023 Honda Accord
# In the above code, we have created a class Car with an
# __init__ method that initializes the attributes of the class. 
# The __init__ method is a special method in Python that is called  
