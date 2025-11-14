# Practice program 19 dice roller program

# ● ┌ ─ ┐ │ └ ┘
import random

"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
while True:
    try:
        num_of_dice = int(input("How many dice?: "))
    except ValueError:
        print("Invalid enter again")
        continue

    for die in range(num_of_dice):
        dice.append(random.randint(1,6))

    # for die in range(num_of_dice):
    #     for line in dice_art.get(dice[die]):
    #         print(line)

    for line in range(5):
        for die in dice:
            print(dice_art.get(die)[line], end = " ")
        print()

    for die in dice:
        total += die
    print(f"total: {total}")

    exit_fnc = input("press q to exit or enter to stay: ")
    if exit_fnc.lower().startswith()== "q":
        print("Exiting...")
        break
