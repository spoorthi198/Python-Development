
from art import logo

# HINT: You can call clear() to clear the output in the console.

print(logo)

bids = {}


def find_heighest_bidder(bidder_record):
    max_bid = 0
    winner = ""

    for bidder in bidder_record:
        bid_amount = bidder_record[bidder]
        if bid_amount > max_bid:
            max_bid = bid_amount
            winner = bidder
    print(f'winner is {winner} and bid amount is ${max_bid}')


bidding_finished = False

while not bidding_finished:
    name = input("Enter the name?")
    price = int(input("enter the bid price?$"))
    bids[name] = price
    should_continue = input("any other user wants to input the bid type 'yes' or 'no'?").lower()
    if should_continue == 'no':
        bidding_finished = True
        find_heighest_bidder(bids)
    elif should_continue == 'yes':
         print('continue')


















