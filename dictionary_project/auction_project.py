#The goal is to ask a person for their name and how much money they want to bid. 
# Then, we ask if there are any other people waiting in the room to bid. If they say "yes", 
# we hide the screen so the next person can't see the previous bid, and we ask the new person 
# for their details. If they say "no", the auction is over, and we look through all the bids 
# to find the biggest one and announce the winner.
#=========================================================================================

bids = {}  #create an empty dictionary to store the bids
biding_finished = False #create a boolean variable to control the while loop
while not biding_finished: #start the while loop where bidding is not finished
    name = input("Enter your name who wants to bid: ") #take the name of the bidder as input
    bid = int(input("Enter your bid amount: $ "))  #take the bid amount as input and convert it to an integer
    bids[name] = bid #store the information into the blank dictionary with the name as the key and the bid amount as the value
    should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    #if no then printing the winner and the bid amount, if yes then clearing the screen by printing 50 new lines to hide the previous bids from the next bidder
    if should_continue == "no": 
         biding_finished = True
         winner = max(bids, key=bids.get)
         print(f"The winner is {winner} with a bid of ${bids[winner]}")
         #clear the screen  by printing 50 new lines to hide the previous bids from the next bidder
    elif should_continue == "yes":
        print("\n" * 50)






