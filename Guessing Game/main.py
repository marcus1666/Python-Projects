import random

def level(mode):
    if mode == "easy":
        lives = 10
    else:
        lives = 5
        
    return lives


def is_correct(guess, number, lives):
    lives_over = False
    while not lives_over:
        
        if guess > number:
            print("Too high \nGuess again")
            lives -= 1
            print(f"You have {lives} attempts remaining to guess the number")
            guess = guess_number()
            if lives == 1:
                lives_over = True
                print("You ran out of lives.... Sorry... GameOver")
        elif guess < number:
            print("Too low \nGuess again")
            lives -= 1
            print(f"You have {lives} attempts remaining to guess the number")
            guess = guess_number()
            if lives == 1:
                lives_over = True
                print("You ran out of lives.... Sorry... GameOver")
        else:
            print("You guessed right, You won")
            lives_over = True
                    
    
def guess_number():
    return int(input("Make a guess: "))

def main():
    print("Welcome to the number Guessing Game! \nI'm thinking of a number between 1 and 100.")
    
    lives = level(input("Choose a difficulty. Type 'easy' or 'hard': "))
    
    print(f"You have {lives} attempts remaining to guess the number")
    comp_number = random.randint(1, 101)
            
    is_correct(guess_number(), comp_number, lives)
    
    
    
main()