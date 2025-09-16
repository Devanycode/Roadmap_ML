from art import logo
bidders = {}
more_bidders = 'yes'
while more_bidders == 'yes':
    print(logo)
    name = input("What is your name?:  ")
    bid = int(input("What is your bid?:  $"))
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.  ")
    bidders[name] = bid
    if more_bidders == 'yes':
        print("\n"*20)

for names, bids in bidders.items():
    if bids == max(bidders.values()):
        print(f"The Winner is {names} with a bid of ${bids}")
        break
