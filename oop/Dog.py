## define a class using the 'class' keyword
class Dog:
    # initializer -> define the attributes needed for the objects 
    # __init__ -> this allows initialization of the class attributes 
    # takes in a mandatory parameter called self
    # self points to the current object in execution
    # the other parameters can be the attributes needed 
    def __init__(self,name , age , breed ):
        self.name = name
        self.age = age
        self.breed = breed 
        
    # object methods -> always pass in self as part of the parameters 
    # bark()
    def bark(self):
        #print(f"{self.name} say woof!")  
        return f"{self.name} say woof!"  
        
## creating objects from the class 
# variable for referencing the object created 
# make a call to the attribute or method to access 
dog1  = Dog("Buddy",3,"Chihuahua")
dog2  = Dog("Rex",4,"German Shepherd")
# to access the attributes simply use the dot notation objectname.attributename , 
# to access the methods simply use the dot notation objectname.mehthodname()
print(f"{dog2.name} is a {dog2.breed} and it's {dog2.age} year's old")
print(dog2.bark())




