class Car:
    def __init__(self): #initializer method, constructor method
        print("Car is created")
        self.name = "BYD"
        self.color = "Red"
        self.speed = 100
        self.brand = "Toyota" #class variable, it is shared by all the objects of the class
    def welcome(self): #method of the class, it is associated with the object of the class
        print("Welcome to the Car class", self.name)
car1 = Car() #c1 is object/instance for class Car, _init_ method is called when we create an object of the class, 
#it is used to initialize the attributes of the class
print(f"Car name is : {car1.name}")
print(f"Car color is : {car1.color}")
print(f"Car speed is : {car1.speed}")
car1.welcome() #welcome is a method of class Car, it is called using the object of the class