def add(n1,n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2

#Todo 2: Add these function into a dictionary as the values. Keys = "+", "-", "*", "/"

operations = {
    "+": add,  # + is Key and add is the value. So, when we call operations["+"], it will return the function add.
    "-": subtract,
    "*": multiply,
    "/": divide
}
#Todo 3: Use the Dictionary operations to perform the calculations. Multiply 4*8 using dictionary
# result = operations["*"](n1=4, n2=8)
# print(result)should_accumulate ==True
def calculator():
    should_accumulate = True
    num1 = float(input("Enter the first number: "))
    while should_accumulate:
        for symbol in operations:  #symbol is the key in the dictionary operations. So, it will print +, -, *, / as key.
            print(symbol)  #print the operations keys +,-,* and /
        opertion_symbol = input("Pick the operation symbol: ")
        num2 = float(input("Enter the second number: "))
        answer = operations[opertion_symbol](n1=num1, n2=num2)  #Here, we are calling the function using the key in the dictionary operations.
        print(f"{num1} {opertion_symbol} {num2} = {answer}")
        continue_calculation = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if continue_calculation == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" *50)
            calculator()  # if start a new calculation if type n then start from the begining top where we have
            # defined the function

calculator()  #Calling the calculator function to start the calculator program.



