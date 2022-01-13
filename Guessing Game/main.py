import random
from art import logo

def level(mode):
    if mode == "easy":
        lives = 10
    else:
        lives = 5
        
    return lives


def is_correct(number, lives):
    """Takes the guess, the number and amount of lives left as parameters
    Then compares to give appropriate retuens"""
    
    while lives > 0:
        print(f"You have {lives} attempts remaining to guess the number")
        guess = guess_number()
        
        if guess == number:
            print("You guessed right, You won")
            return
            
        elif guess > number:
            print("Too high")
            lives -= 1
            
      
        elif guess < number:
            print("Too low")
            lives -= 1
            
         
    print(f"You ran out of lives.... Sorry... GameOver\nThe number was {number}")                
    
def guess_number():
    return int(input("Make a guess: "))

def main():
    print(logo)

    print("Welcome to the number Guessing Game! \nI'm thinking of a number between 1 and 100.")
    
    lives = level(input("Choose a difficulty. Type 'easy' or 'hard': "))
    comp_number = random.randint(1, 101)
            
    is_correct(comp_number, lives)
 
    
main()