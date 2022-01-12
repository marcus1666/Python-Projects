
import random   
    
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

"""rock = 0
paper = 1
scissors = 2"""
options = [rock, paper,scissors]
comp_choices = random.choice(options)

user_num = int(input("Which do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
user_choice = ""

if user_num == 0:
    user_choice = rock
elif user_num == 1:
    user_choice = paper
else:
    user_choice = scissors
    
    
state = ""
if user_choice == rock and comp_choices == scissors:
    state = "You win"
elif user_choice == scissors and comp_choices == paper:
    state = "You win"
elif user_choice == paper and comp_choices == rock:
    state = "You win"
elif user_choice == comp_choices:
    state = "Draw"
elif user_choice == scissors and comp_choices == rock:
    state = "You Lose"
elif user_choice == paper and comp_choices == scissors:
    state = "You Lose"
elif user_choice == rock and comp_choices == paper:
    state = "You Lose"
    
    
print(user_choice)
print("Computer Choose:\n" + comp_choices)
print(state)