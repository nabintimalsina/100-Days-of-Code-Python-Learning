#The goal is to ask a person for their name and how much money they want to bid. 
# Then, we ask if there are any other people waiting in the room to bid. If they say "yes", 
# we hide the screen so the next person can't see the previous bid, and we ask the new person 
# for their details. If they say "no", the auction is over, and we look through all the bids 
# to find the biggest one and announce the winner.
#=========================================================================================
# from Function_Project import art
# print(art.logo)

bids = {}

while True:
    name = input("Enter your name who wants to bid: ")
    try:
        bid = int(input("Enter your bid amount: $ "))
    except ValueError:
        print("Please enter a valid number for the bid.")
        continue

    bids[name] = bid

    more = input("Are there any other bidders? Type 'yes' or 'no': ").strip().lower()
    if more == 'no':
        break
    # simple way to hide previous bids
    print("\n" * 50)

# determine        
if bids:
    winner = max(bids, key=bids.get)
    print(f"The winner is {winner} with a bid of ${bids[winner]}")
else:
    print("No bids were placed.")