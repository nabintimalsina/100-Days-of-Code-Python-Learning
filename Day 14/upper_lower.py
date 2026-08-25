#Display art
from art import logo, vs
import random
from game_data import data

def format_data(account):
    """Format the account data into printable format"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(user_guess, a_followers, b_followers):
    """Take a user guess and the follower counts and returns if they got it right"""
    if a_followers > b_followers and user_guess =="a":
        return True
    else:
        return False

print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)
while game_should_continue:
    #Generate a random account from the game data
    account_a= account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)  #account be will be regenerated to prevent account_a and account_b pickhup different data

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    #Ask a user for a guess
    guess = input("Who has more followers? Type 'A' or 'B' :").lower()

    #clear the screen
    print("\n" *20)
    print(logo)
    #Check if user is correct
    ##Get followers count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    ##Use if statement to check if user is correct

    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    #Give user a feedback on their guess

    if is_correct:
        score += 1
        print(f"You're Right !! Current score is {score}")
    else:
        print(f"Sorry, That's Wrong!!, Final Score : {score}")
        game_should_continue = False

    #Score Keeping


    #Make the game repeatable

    #Making account at pistion B become the next account of Position A

