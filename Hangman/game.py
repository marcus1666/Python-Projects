#Step 1 
import random
from hangman_words import word_list
from hangman_art import stages, logo


print(logo)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.

lives = 6
win = False  

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
random_word = random.choice(word_list)

display = []


for i in range(len(random_word)):
    display.append("_")
end_of_game = False
print(display)
    
while not end_of_game:


    #TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    letter_check = True
    
    while letter_check:
        user_guess = input("Guess a letter: ")
        letter_check = False
        
        if user_guess in display:
            print(f"You've already guessed {user_guess.upper()}")
            print(f"{' '.join(display)}")
            print(stages[lives])
            letter_check = True
        
    #TODO-2: - Loop through each position in the chosen_word;
    #If the letter at that position matches 'guess' then reveal that letter in the display at that position.
    #e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
    index = 0
    correct = False
    for i in random_word:
        if i == user_guess.lower():
            
            display[index] = user_guess.upper()
            correct = True

        
        index += 1
    #reduce the lives outside the above loop
    if user_guess.lower() not in random_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        lives -= 1
        print(f"you guessed {user_guess.upper()}, that's not in the word. You lose a life.")       
        if lives == 0:
            end_of_game = True

            print("You lose.")
            print(f"The word is {random_word}")
            
    print(f"{' '.join(display)}")
    print(stages[lives])        

    #breaks the loop that keeps asking the user to input a letter

    if "_" not in display:
        end_of_game = True
        print(f"{' '.join(display)}")
        print(stages[lives])
        print("You Win.") 

    #TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
    #Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

