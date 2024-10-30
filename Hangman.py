import random 
from hangman_art import stages,logo                #imports the logo to print at the start of the game
from hangman_word import word_list                 #imports the word list to choose a random word
chosen_word = random.choice(word_list)

placeholder = ""

for letter in range(len(chosen_word)):
    placeholder += '_'                            #prints blank spaces for each letter in chosen word 

print(logo)
print(placeholder)
print(chosen_word)

game_over = False                                
correct_letters = []                              #storing each correct guess user inputs
lives = 6                                         #number of lives the player has

while not game_over:
    guess_letter = input("Guess letter: ").lower()

    if guess_letter in correct_letters:                                #to check if player has already guessed a letter, no lives will be reduced
        print(f"You have already guessed '{guess_letter}'.")
    
    display = ""
    
    for letter in chosen_word:
        if guess_letter == letter:
            display += letter                                    #for each correct guess, replace the blanks with the letter
            correct_letters.append(letter)
        elif letter in correct_letters:                          #for each correct guess, add the letters to correct_letter list
            display += letter                                
        else:
            display += "_"                                       
    print(display)
    
    if "_" not in display:                                       #if no blanks are there, then player has won
        game_over = True
        print("You win.")
    

    if guess_letter not in chosen_word:                         #deducting a life for each incorrect guess
        lives -= 1
        print(f"You guessed '{guess_letter}', that is not in the word. You lose a life. ")
        print(f"You have {lives}/6 lives left.")
        
        if lives == 0:                                          #if lives is zero, then player lose the game
            game_over = True
            print ("You lose.")
    
        print (stages[lives])                                   #print the appropriate figure for represent remaining lives
