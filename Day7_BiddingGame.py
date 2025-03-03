bid_list = {}
more_bidder = 'yes'
while more_bidder == 'yes' :
    bidder_name = input("What is your name?: ")
    bidder_amount = int(input("What is your bid?: $"))
    bid_list[bidder_name] = bidder_amount
    more_bidder = input("Are there any other bidders? Type 'yes' or 'no':\n").lower()

print('The maximum bidd amount is given by', max(bid_list))


