import os

bids = {}
bidding_finished = False


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def find_highest_bidder():
    highest_value = 0
    winner = ""
    for bidder in bids:
        current_value = bids[bidder]
        if current_value > highest_value:
            highest_value = current_value
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_value}")


while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder()
    elif should_continue == "yes":
        clear_screen()
    else:
        print("Invalid input. Please type 'yes' or 'no'.")