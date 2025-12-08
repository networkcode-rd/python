
name = str(input("What is your name?:"))
price = int(input("What is your bid?: Rs."))

def compare_bids(bid_history):
    winner = ""
    highest_bid_amount = 0
    for bidder in bid_history:
        bid_amount = bid_history[bidder]
        if bid_amount > highest_bid_amount:
            highest_bid_amount = bid_amount
            winner = bidder
    
    print(f"The winner is {winner} with a bid of Rs.{highest_bid_amount}")

auction_bid = {}
auction_bid[name] = price

should_continue = input("Are there any new biders? Type 'Yes' or 'No'").lower()

proceed_bidding = True
while proceed_bidding:
    name = str(input("What is your name?:"))
    price = int(input("What is your bid?: Rs."))
    auction_bid[name] = price
    should_continue = input("Are there any new biders? Type 'Yes' or 'No'").lower()

    if proceed_bidding == "no":
        proceed_bidding = False
        compare_bids(auction_bid)
    elif proceed_bidding == "yes":
        print("\n *20")







