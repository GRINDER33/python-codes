# Practice program 23 Hangman Game 
# Use word_list_animals.py and words_list_fruits.py as word dictionary

import random 
import time

# dictionary of key:()
hangman_art = {0:("      ┌---┐          ",
                  "      |              ",
                  "      |              ",
                  "      |              ",
                  "      |              "),
              1: ("      ┌---┐          ",
                  "      |   o          ",
                  "      |              ",
                  "      |              ",
                  "      |              "),
              2: ("      ┌---┐          ",
                  "      |   o          ",
                  "      |   |          ",
                  "      |              ",
                  "      |              "),
              3: ("      ┌---┐          ",
                  "      |   o          ",
                  "      |  /|          ",
                  "      |              ",
                  "      |              "),
              4: ("      ┌---┐          ",
                  "      |   o          ",
                  "      |  /|\\        ",
                  "      |              ",
                  "      |              "),
              5: ("      ┌---┐          ",
                  "      |   o          ",
                  "      |  /|\\        ",
                  "      |  /           ",
                  "      |              "),
              6: ("      ┌---┐          ",
                  "      |   o    DEAD! ",
                  "      |  /|\\        ",
                  "      |  / \\        ",
                  "      |              ")}

def display_man(wrong_guesses):                   # Displays the part of man after wrong guesses
    print("______________________________")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("______________________________")

def display_hint(hint):                           # Displays the hint in the form of "_" and joins it to hint
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))                       # Displays answer with " " in between letters

def slow_print(text, delay=0.05):
    for letter in text:
        print(letter, end="", flush=True)
        time.sleep(delay)

def main():
    
    time.sleep(0.2)
    print("______________________________")
    print()
    print("           HANGMAN            ")
    print("______________________________")

    answer = random.choice(words).lower()         # Choses a random word from the provided word dictionary
    hint = ["_"] * len(answer)                    # Displays the hint as "_" answer number of times
    wrong_guesses = 0
    guessed_letters = set()

    while True:
        print()
        print(f"Wrong Guesses: {wrong_guesses}")
        display_man(wrong_guesses)
        print()
        display_hint(hint)
        print()
        
        time.sleep(0.3)
        slow_print("Enter a letter: ", 0.05)
        guess = input().lower() 
        print("____________________________________|")
        if len(guess) != 1 or not guess.isalpha():# Checks for invalid input like words or digits
            print("Invalid input.")
            time.sleep(0.3)
            continue
        
        if guess in guessed_letters:
            print(f"{guess} is already guessed!")
            time.sleep(0.3)
            continue
        
        guessed_letters.add(guess)                # Adds the guessed letters in list guesses_letters so code doesnt add it again

        if guess in answer:                       # Replaces the guessed letter if corrct with the "_" in hint
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
            time.sleep(0.3)
        else:
            wrong_guesses += 1
        
        if "_" not in hint:  
            print(f"Wrong Guesses: {wrong_guesses}")                     
            display_man(wrong_guesses)            # Gives out the win message if there are no "_" left in hint meaning the word is guessed
            display_answer(answer)
            print("****************")
            print("YOU WIN!")
            print()
            print("****************")
            break
            
        elif wrong_guesses >= len(hangman_art) - 1:
            print(f"Wrong Guesses: {wrong_guesses}")
            display_man(wrong_guesses)            # Gives out the lost message if all lives are lost 
            display_answer(answer)
            print("****************")
            print("YOU LOSE!")
            print()
            print("****************")
            break

if __name__ == '__main__':
    
    while True:
        try:
            guess_type = input("What do you want to guess about(A: for animals / F: for fruits): ").lower()  
            if guess_type == "a":                         # Asks user for the type of guess
                        from word_list_animals import words
            elif guess_type == "f":
                        from words_list_fruits import words
            elif guess_type not in ("a", "f"):
                        print("Invalid choice! Please select A or F.")
                        continue
        except KeyboardInterrupt:                         # Present crashes for keyboard button interrupt like ctrl + c
                        print("\nPlease Enter the type!")
                        continue
        if guess_type == "a":                     
            print(f"Guessing Animals... ")
            print()
        else:
            print(f"Guessing Fruits...")
            print()
        
        time.sleep(0.3) 

        main() 
        exit_fnc = input("Press Q to exit or Enter to play again: ").lower()
        if exit_fnc != "q":                       # Breaks the loop
            continue
        else:
            time.sleep(0.3)
            print("Exiting...")
            break     




