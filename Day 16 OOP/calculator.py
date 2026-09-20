
class Calculator:

    @staticmethod
    def add (a, b):
        return a+b
    @staticmethod              
    def subtract (a, b):
        return a-b
    @staticmethod
    def multiply (a, b):
        return a*b
    @staticmethod   
    def divide (a, b):
        if b == 0:
            return "Error: Division by zero"
        return a/b
    @staticmethod
    def modulus (a, b):
        return a%b
# Input collection happens in the main program execution flow which is outside the class definition. The Calculator class is responsible for performing calculations, 
# while the main program handles user input and output. This separation of concerns makes the code more organized and easier to maintain.   
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
cal = Calculator()
# cal.add(5,3)
print(cal.add(a,b))
# cal.subtract(5,3)
print(cal.subtract(a,b))
# cal.multiply(5,3)
print(cal.multiply(a,b))
# cal.divide(5,3)
print(cal.divide(a,b))
# cal.modulus(5,3)
print(cal.modulus(a,b))
