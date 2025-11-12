# one object references another 
class Driver:
    def __init__(self, name):
        self.name = name 
        
class Car:
    def __init__(self, model):
        self.model = model
        
    def assign_driver(self,driver):
        # driver references an actual object 
        self.driver = driver  # association 
        print(f"{driver.name} is now driving {self.model}")
        
        
driver1 = Driver("Joseph")
driver2 = Driver("Jane")
car1  = Car("Toyota Corolla")
car1.assign_driver(driver1)