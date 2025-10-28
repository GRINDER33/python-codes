# Practice program 21 Slot machine
import random
import time
import sys

def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']

    return [random.choice(symbols) for symbol in range(3)]


def print_row(row):
    print(" | ".join(row))

def animated_spin():
    """Show spinning animation and return final row"""
    for _ in range(10):  # 10 “frames” of spinning
        temp_row = spin_row()
        print_row(temp_row)
        time.sleep(0.1)
        # Move cursor up to overwrite previous row
        sys.stdout.write("\033[F")  # ANSI escape code: move cursor up one line
    # Final row
    final_row = spin_row()
    print_row(final_row)
    return final_row
  
def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 20
    return 0
    
def main():
    balance = 100
    
    print("----------------------------")
    print("Welcome to Python Slot")
    print("Symbol: 🍒 🍉 🍋 🔔 ⭐ ")
    print("----------------------------")

    while balance > 0:
        print(f"Curent Balance: ${balance}")

        bet = input("Place you bet amount: ")
        if not bet.isdigit():
            print("Please enter a valid number.")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds!")
            continue

        if bet <= 0:
            print("Bet must be Greater than 0")
            continue

        balance -= bet
        
        row = spin_row()
        print("Spinning...\n")
        row = animated_spin()

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("Sorry you lost this round")
        
        balance += payout

        exit_fnc = input("Do you want to spin again? (Y/N): ").upper()

        if exit_fnc != "Y":
            break
    
    print("------------------------------------------------")
    print(f"Game Over! Your Final Balance is ${balance}")
    print("------------------------------------------------")


if __name__ == '__main__':
    main()