#the Secret Auction Program



logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

bids = {}

#bids[name] = price: This line adds a key-value pair to the bids dictionary. 
    #The key is the name of the participant (stored in the variable name), 
    #and the value is the bid made by that participant (stored in the variable price). 
    #This effectively records each participant's bid in the bids dictionary.

def highest_bidding_amount(bidding_record):
    #biding_record = {"Hrishikesh": 123, "XYZ": 213}
    highest_bid = 0  #variable to store value 
    winner = " "
    for bid_person in bidding_record:     #all bidding_record will comes in bid_person
        bid_amount = bidding_record[bid_person]  #all bid_person of bidding_record comes in bid_amount
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bid_person
    print(f"The winner is {winner} with the bid of ${highest_bid}")        


bidding_finished = False

while not bidding_finished:  #not bidding_finished = not False = True  
    #bidding continues till it won't come "False"
    name = input("What is your name? ")
    price = int(input("What is your bid? $"))
    bids[name] = price
    should_continue = input("Are there any one 'yes' or 'no'? ")
    if should_continue == "no":
        bidding_finished = True
        highest_bidding_amount(bids)
    elif should_continue == "yes":
        bids.clear()    
