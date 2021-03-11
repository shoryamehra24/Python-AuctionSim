from os import system
from art import logo

cls = lambda: system('cls')

print(logo)

print("Welcome to the silent auction program.")

start_game = True 

auction_details = {}

while start_game:
    name = input("What is your name? \n")
    bid = int(input("What is your bid? \n$"))
    auction_details[name] = bid
    bidders = input("Are there anymore bidders? yes or no \n")
    start_game = False
    cls()
    if bidders == "yes":
        start_game = True

max_bid = 0
max_bidder = ""

for k,v in auction_details.items():
    if v > max_bid:
        max_bid = v
        max_bidder = k

print(f'{max_bidder} has placed the highest bid of ${max_bid}.')





