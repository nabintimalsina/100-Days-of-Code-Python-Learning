from random import randint
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURN = 5
#Function to check the user gueess against actual answer
def check_answer(user_guess, actual_answer,turns):
    """Check answer againts the guess returns the number of turns remaining"""
    if user_guess>actual_answer:
        print("Too High")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"You got it!! The answer is {actual_answer}")

#Function to set difficulty
def set_difficulty():
    level = input(f"Choose a difficulty. Type 'easy' or 'hard' \n").lower()
    if level =="easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURN
def game():
    #choosing a random number between 1 and 100
    print("Welcome to the Number Guessing Game")
    print("I am thinking of a number between 1 and 100")
    answer = randint(1, 100)
    print(f"The correct answer is {answer}")

    turns = set_difficulty()
    guess = 0
    while guess !=answer:
        print(f"You have {turns} attempt remaining to guess the number:")
        #Let the user guess a number
        guess = int(input("Make a Guess"))
        if turns <1:
            print("YOu have run out of guesses, You LOOSE")
            return
        elif guess !=answer:
            print("Guess Again : ")
        turns= check_answer(guess,answer,turns)
game()

