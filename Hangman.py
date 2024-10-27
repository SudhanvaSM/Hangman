import random 
from hangman_art import stages,logo
from hangman_word import word_list

chosen_word = random.choice(word_list)

placeholder = ""

for letter in range(len(chosen_word)):
    placeholder += '_'

print(logo)
print(placeholder)
print(chosen_word)

game_over = False
correct_letters = []
lives = 6

while not game_over:
    guess_letter = input("Guess letter: ").lower()

    if guess_letter in correct_letters:
        print(f"You have already guessed '{guess_letter}'.")
    
    display = ""
    
    for letter in chosen_word:
        if guess_letter == letter:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)
    
    if "_" not in display:
        game_over = True
        print("You win.")
    

    if guess_letter not in chosen_word:
        lives -= 1
        print(f"You guessed '{guess_letter}', that is not in the word. You lose a life. ")
        print(f"You have {lives}/6 lives left.")
        
        if lives == 0:
            game_over = True
            print ("You lose.")
    
        print (stages[lives])