# Practice program 18 rock paper scissors

import random

options = ("rock", "paper", "scissors")
running = True

while running:

    player = None
    computer = random.choice(options)
   
    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")


    print(f"Player: {player}")
    print(f"Computer : {computer}")

    if player == computer:
        print("Tie!")
    elif player == "rock" and computer == "scissors":
        print("You win")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")
        
    exit_fnc = input("Play again ? (y/n): ").lower()
    if not exit_fnc == "y":
        running = False
print("Thanks for playing.")