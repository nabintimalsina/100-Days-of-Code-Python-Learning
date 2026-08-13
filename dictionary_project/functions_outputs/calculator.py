number1 = int(input("What is the first number?: "))
number2 = int(input("What is the second number?: "))
operator = input("Which operation would you like to perform? (+, -, *, /, %): ")

while operator not in ["+", "-", "*", "/","%"]:
    print("Invalid operator. Please choose from +, -, *, /, or %.")
    operator = input("Which operation would you like to perform? (+, -, *, /, %): ")
continue_calculation = input("Do you want to perform another calculation? Type 'yes' or 'no': ").lower()
should_continue = True
while should_continue:
    def add(n1, n2):
        if operator == "+":
            return n1 + n2
    def subtract(n1, n2):
        if operator == "-":
            return n1 - n2
    def multiply(n1, n2):
        if operator == "*":
            return n1 * n2
    def divide(n1, n2):
        if operator == "/":
            return n1 / n2
    def modulo(n1, n2):
        if operator == "%":
            return n1 % n2
    addition = add(number1, number2)
    subtraction = subtract(number1, number2)
    multiplication = multiply(number1, number2)
    division = divide(number1, number2)
    modulo_result = modulo(number1, number2)

    print(f"Addition: {addition}")
    print(f"Subtraction: {subtraction}")
    print(f"Multiplication: {multiplication}")
    print(f"Division: {division}")
    print(f"Modulo: {modulo_result}")
while continue_calculation == "no":
    should_continue = False
    print("Thank you for using the calculator. Goodbye!")
    break
