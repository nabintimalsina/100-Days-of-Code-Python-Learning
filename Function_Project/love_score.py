# def calculate_love_score(fname, lname):
#     # true = input("Enter the name TRUE: \n").lower()
#     # love = input("Enter the name LOVE: \n").lower()
    
#     # concate = true + " "+ love
#     # print(f"Concatenate letter is : {concate}")
#     print(f"First and Last name is : {fname} {lname}")
# calculate_love_score("true ", "love")    
    
# from itertools import count


# def calculate_love_score():
#     true = input("Enter the name TRUE: \n").lower()
#     love = input("Enter the name LOVE: \n").lower()
    
#     concate = true + " "+ love
#     print(f"Concatenate letter is : {concate}")
#     count_love = count(love)
#     count_true = count(true)
#     number_concatenate = count_love + count_true
#     print(f"Total number of letters in concatenated string: {number_concatenate}")
#     print(f"Count of LOVE letters: {count_love}")
#     print(f"Count of TRUE letters: {count_true}")

# calculate_love_score()     

def calculate_love_score(name1, name2):
    # Convert names to lowercase
    # name1 = name1.lower()
    # name2 = name2.lower()

    # Concatenate the names
    concatenated_names = name1 + " " + name2  
    lower_names = concatenated_names.lower()  #kanya west kim kardashian
    print(f"Concatenated names: {lower_names}")
    #count the letters for the word TRUE
    t = lower_names.count('t')
    r = lower_names.count('r')
    u = lower_names.count('u')
    e = lower_names.count('e')
    #add them upto get the first digit
    first_digit = t + r + u + e  # 1+1+1+1+1 truee (1 e from Love) = 5

    #Count the letters for the word LOVE
    l = lower_names.count('l')
    o = lower_names.count('o')
    v = lower_names.count('v')
    e = lower_names.count('e')
    #add them upto to get the second digit
    second_digit = l + o + v + e # 1+1+1+1 e(from True) = 5
    love_score = str(first_digit) + str(second_digit)
    print(f"Your love score is: {love_score}")
calculate_love_score("Nabin", "Timalsina")
