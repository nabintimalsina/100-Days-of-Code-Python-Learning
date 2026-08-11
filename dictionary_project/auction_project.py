#The goal is to ask a person for their name and how much money they want to bid. 
# Then, we ask if there are any other people waiting in the room to bid. If they say "yes", 
# we hide the screen so the next person can't see the previous bid, and we ask the new person 
# for their details. If they say "no", the auction is over, and we look through all the bids 
# to find the biggest one and announce the winner.
#=========================================================================================
# from Function_Project import art
# print(art.logo)

name = input("Enter you name who wants to bid: ")
bid = int(input("Enter your bid amount: $ "))

winner = {name: bid}
print(winner)