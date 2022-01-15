import random
from game_data import data
from art import logo, vs
import os
class game():

    
    def __init__(self):
        self.data = data
    
    def game_info(self, selected):
        
        used = True
        while used:
            details_one = random.choice(data)
            if details_one not in selected:
                selected.append(details_one)
                return [selected[-2], details_one]
                
    def display(self, first, second):
        first_name = first["name"]
        first_description = first["description"]
        first_country = first["country"]
        
        second_name = second["name"]
        second_description = second["description"]
        second_country = second["country"]
        
        print(f"Compare A: {first_name}, a {first_description}, from {first_country}")
        print(vs)
        print(f"Against B: {second_name}, a {second_description}, from {second_country}")
        
        
    def compute(self, first, second):
        A_followers = first["follower_count"]
        B_followers = second["follower_count"]
        
        if A_followers > B_followers:
            return "a"
        else:
            return "b"
            
        
            
            
def main():
    print(logo)
    selected = []
    selected.append(random.choice(data))     
    play = game()
    score = 0
    
    lets_play = True
    while lets_play:
        details_list = play.game_info(selected)
        
        play.display(details_list[0], details_list[1])
        
        user_input = input("Who has more followers? Type 'A' or 'B': ").lower()
        correct_answer = play.compute(details_list[0], details_list[1])
        
        if user_input == correct_answer:
            score += 1
            os.system('cls||clear')
            print(logo)
            print(f"You are right, current score: {score}")
        else:
            os.system('cls||clear')
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            lets_play = False
    
    
    
if __name__ == '__main__':
    main()