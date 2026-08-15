def leap_year_check():
    leap_year = input("Enter a year: ")
    if leap_year.isdigit(): #Check if the text is made of safe digits. 
        #This is our Security Guard! It prevents the program from crashing later on.
        leap_year = int(leap_year)
        if leap_year % 4 == 0 and leap_year %100 ==0 and leap_year % 400 == 0:
            print(f"{leap_year} is a leap year.")
        else:
            print(f"{leap_year} is not a leap year.")
leap_year_check()

