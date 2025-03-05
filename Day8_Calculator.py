bid_list = {}


def max_bid(bidding_dictionary):
    max_value = max(bidding_dictionary.values())
    max_key = [key for key in bidding_dictionary if bidding_dictionary[key] == max_value]
    print('The maximum bid amount is given by', *max_key)


continue_bidding = True
while continue_bidding:
    bidder_name = input("What is your name?: ")
    bid_amount = int(input("What is your bid?: $"))
    bid_list[bidder_name] = bid_amount
    should_continue = input("Are there any other bidders? Type 'yes' or 'no':\n").lower()
    if should_continue == 'yes':
        print("\n" * 100)
    else:
        max_bid(bid_list)
        continue_bidding = False
