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

