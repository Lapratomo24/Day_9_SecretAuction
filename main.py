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

from os import system

# list_of_bidders = []

# def bidders(name, bid):
#     bidders = {}
    
#     bidders["name"] = name
#     bidders["bid"] = bid
#     list_of_bidders.append(bidders)

def highest_bidder(people):
    winning_bid = 0
    winner = ""
    
    for person in people: #people as a list
        bid_amount = people[person]
        if bid_amount > winning_bid:
            winning_bid = bid_amount
            winner = person
    print(f"The item goes to our highest bidder, {winner}! Congratulations!")

print(logo)

bidders = {}
auction_end = False

while not auction_end:
    name = input("Enter your name: ")
    bid = int(input("Enter your bid amount: $"))
    
    bidders[name] = bid

    last_bid = input("Do I hear another bid? Type 'yes' or 'no' --> ")
    if last_bid == 'yes':
        system("cls")
    else:
        auction_end = True
        highest_bidder(bidders)
        
        