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

list_of_bidders = []

def bidders(name, bid):
    bidders = {}
    
    bidders["name"] = name
    bidders["bid"] = bid
    list_of_bidders.append(bidders)

def highest_bidder(people):
    winner = people[0]
    
    for person in people[1:]:
        if person["bid"] > winner["bid"]:
            winner = person

print(logo)

auction_end = False

while not auction_end:
    name = input("Enter your name: ")
    bid = int(input("Enter your bid amount: $"))
    
    bidders(name, bid)

    last_bid = input("Do I hear another bid? Type 'yes' or 'no' --> ")
    if last_bid == 'yes':
        system("cls")
    else:
        auction_end = True
        highest_bidder(list_of_bidders)
        print(f"The item goes to our highest bidder, {name}! Congratulations!")
        