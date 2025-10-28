# Practice program 24 Password gen

import random
import string
import time

pass_lib = string.punctuation + string.digits + string.ascii_letters
pass_lib = list(pass_lib)

is_running = True

# Function for slow printing
def slow_print(text, delay=0.01):
    for letter in text:
        print(letter, end="", flush=True)
        time.sleep(delay)

# Function to generate password
def generate_password(length):
    password = ''
    for _ in range(length):
        password += random.choice(pass_lib)
    return password

# Function to check password strength
def check_strength(password):
    length = len(password)
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    score = sum([has_lower, has_upper, has_digit, has_symbol])

    # Determine strength
    if length < 6 or score <= 1:
        return "Weak 🔴"
    elif 6 <= length < 10 and score >= 2:
        return "Medium 🟡"
    elif length >= 10 and score >= 3:
        return "Strong 🟢"
    else:
        return "Very Strong 🟣"
    

def main():
    
    print("------------------------------")
    print("      Password Generator      ")
    print("------------------------------")

    while is_running:
        try:
            slow_print("Enter desired password length (4-32): ")
            pass_lngth = int(input())
            print()  # For better readability

            if 4 <= pass_lngth <= 32:
                generated_password = generate_password(pass_lngth)

            elif pass_lngth < 4:
                slow_print("Password length too short! Minimum is 4 characters.\n")
                print("----------------------------------------") # For better readability
                print() # For better readability
                continue

            elif pass_lngth > 32:
                slow_print("Password length too long! Maximum is 32 characters.\n")
                print("----------------------------------------") # For better readability
                print() # For better readability
                continue

        except ValueError:  
            print()  # For better readability
            slow_print("Invalid input! Please enter a number between 4 and 32.\n")
            print("----------------------------------------") # For better readability
            print() # For better readability
            continue

        # Print the generated password

        strength = check_strength(generated_password)

        slow_print(f"Generated Password: {generated_password}\n")
        print()  # For better readabilit
        slow_print(f"Password Strength: {strength} \n")
        print()  # For better readability
        
        # Ask user if they want to generate another password

        exit_fnc = input("Generate another password? (y/n): ").strip().lower()
        if exit_fnc.startswith('n'):
            slow_print("Exiting Password Generator. Goodbye!\n")
            break
        else:
            print("----------------------------------------")  # For better readability
            print()

# Run the main function
if __name__ == "__main__":
    main()

            



