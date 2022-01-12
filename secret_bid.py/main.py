from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo
print(logo)
bid_dic = {}

continue_bidding = True

while continue_bidding:
    
    name = input("What is your name? ")
    amount = int(input("How much do you want to bid? $"))

    bid_dic[name] = amount

    bid_question = input("Is there anyone else left to bid? ").lower()
    if bid_question == "yes":
        clear()
    
    elif bid_question == "no":
        continue_bidding = False
        largest_bid = 0
        for name in bid_dic:
            if bid_dic[name] > largest_bid:
                largest_bid = bid_dic[name]
        for name in bid_dic:           
            if bid_dic[name] == largest_bid:
                print(f"The winner of the bid is {name} with ${largest_bid}")
