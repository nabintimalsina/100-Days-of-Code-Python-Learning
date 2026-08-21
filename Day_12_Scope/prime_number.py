def is_prime():
    while True:
        number = int(input("Enter the number: "))
        for i in range (2, number):
            if number % i ==0:
                print(f"{number} is not a prime")
                break
        else:
            print(f"{number} is prime ")
        if number <1:
            print("Please enter the number greater than 1")
is_prime()