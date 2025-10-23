# Practice program 25 Password Manager

import os
import time
import string
import random

pass_lib = string.punctuation + string.digits + string.ascii_letters # all character types
pass_lib = list(pass_lib)

file_path = "F:/Password_Manager.txt"

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

# Simple password generation
def pass_input():
        try:
            slow_print("Enter desired password length (4-32): ")
            pass_lngth = int(input())
            print()  # For better readability

            if 4 <= pass_lngth <= 32:
                generated_password = generate_password(pass_lngth)
                slow_print(f"Generated Password: {generated_password}\n")

                # Check and display password strength
                strength = check_strength(generated_password)
                slow_print(f"Password Strength: {strength}\n")

            elif pass_lngth < 4:
                slow_print("Password length too short! Minimum is 4 characters.\n")
                print("----------------------------------------") # For better readability
                print() # For better readability
                return

            elif pass_lngth > 32:
                slow_print("Password length too long! Maximum is 32 characters.\n")
                print("----------------------------------------") # For better readability
                print() # For better readability
                return

        except ValueError:  
            print()  # For better readability
            slow_print("Invalid input! Please enter a number between 4 and 32.\n")
            print("----------------------------------------") # For better readability
            print() # For better readability

        print()  # For better readability

# For generating password with name and saveing to txt file
def pass_name_input():
        try:
            slow_print("Enter the name for the password: ")
            pass_name = str(input())
            print()  # For better readability

            slow_print("Enter Email: ")
            email = str(input())
            print()  # For better readability

            slow_print("Enter desired password length (4-32): ")
            pass_lngth = int(input())
            print()  # For better readability

            if 4 <= pass_lngth <= 32:  
                generated_password = generate_password(pass_lngth)

            elif pass_lngth < 4:
                slow_print("Password length too short! Minimum is 4 characters.\n")
                print("----------------------------------------") # For better readability
                print() # For better readability
                return

            elif pass_lngth > 32:
                slow_print("Password length too long! Maximum is 32 characters.\n")
                print("----------------------------------------") # For better readability
                print() # For better readability
                return

        except ValueError:  
            print()  # For better readability
            slow_print("Invalid input! Please enter a number between 4 and 32.\n")
            print("----------------------------------------") # For better readability
            print() # For better readability
            return

        slow_print(f"Username: {pass_name} \nEmail: {email} \nGenerated Password: {generated_password}\n")
        print()  # For better readability

        # Check and display password strength
        strength = check_strength(generated_password)
        slow_print(f"Password Strength: {strength}\n")
        print()  # For better readability

        # Prompt to save the password

        save_perm = input("Do you want to save this password? (y/n): ").strip().lower()
        print()  # For better readability

        if save_perm.startswith("") or save_perm.startswith('y'):        

            chances = 3 # Number of attempts
            correct_pass = "admin123" # Example access password
            print()  # For better readability
            save_access = True

            while save_access:     # Loop until valid input or attempts exhausted

                slow_print("Enter password to confirm saving: ")
                access_pass = str(input())
                print()  # For better readability

                if access_pass == correct_pass:

                    try:
                        with open(file_path, "a") as file:
                            file.write(f"\n---------------------------\nUsername: {pass_name}\nEmail: {email} \nPassword: {generated_password}\n")
                            print(f"txt file '{file_path}' was appended")
                            print()  # For better readability

                    except FileNotFoundError:
                        slow_print("Error: File path not found. Please check your drive or path.\n")
                        print()  # For better readability  
                    save_access = False # Exit the loop after error
                else:
                    chances -= 1
                    slow_print(f"Incorrect password! Password not saved. You have {chances} attempts left.\n")
                    slow_print("-------------------------------------------------------\n")
                    print()  # For better readability
                    if chances == 0:
                        slow_print("No attempts left! Password not saved.\n")
                        print()  # For better readability
                        save_access = False # Exit the loop after exhausting attempts

        else:
            slow_print("Password not saved.\n")
            print()  # For better readability

# For manual password with name and saveing to txt file
def manual_pass_name_input():
        try:
            slow_print("Enter the name for the password: ")
            pass_name = str(input())
            print()  # For better readability

            slow_print("Enter Email: ")
            email = str(input())
            print()  # For better readability

            slow_print("Enter password: ")
            password = str(input())
            print()  # For better readability

        except Exception:
            print()  # For better readability
            slow_print("An error occurred. Please try again.\n")
            print("----------------------------------------") # For better readability
            print() # For better readability

        slow_print(f"Username: {pass_name} \nEmail: {email} \nPassword: {password}\n")
        print()  # For better readability

        # Check and display password strength
        strength = check_strength(password)
        slow_print(f"Password Strength: {strength}\n")
        print()  # For better readability

        save_perm = input("Do you want to save this password? (y/n): ").strip().lower()
        print()  # For better readability

        if save_perm.startswith("") or save_perm.startswith('y'):

            chances = 3 # Number of attempts
            correct_pass = "admin123" # Example access password
            print()  # For better readability
            save_access = True

            while save_access:     # Loop until valid input or attempts exhausted

                slow_print("Enter password to confirm saving: ")
                access_pass = str(input())
                print()  # For better readability

                if access_pass == correct_pass:

                    try:
                        with open(file_path, "a") as file:
                            file.write(f"\n---------------------------\nUsername: {pass_name}\nEmail: {email} \nPassword: {password}\n")
                            print(f"txt file '{file_path}' was appended")
                            print()  # For better readability

                    except FileNotFoundError:
                        slow_print("Error: File path not found. Please check your drive or path.\n")
                        print()  # For better readability  
                    save_access = False # Exit the loop after error
                else:
                    chances -= 1
                    slow_print(f"Incorrect password! Password not saved. You have {chances} attempts left.\n")
                    slow_print("-------------------------------------------------------\n")
                    print()  # For better readability
                    if chances == 0:
                        slow_print("No attempts left! Password not saved.\n")
                        print()  # For better readability
                        save_access = False # Exit the loop after exhausting attempts

        else:
            slow_print("Password not saved.\n")
            print()  # For better readability

def show_passwords():
    
    chances = 3 # Number of attempts
    correct_pass = "admin123" # Example access password

    is_valid = True # Flag to control the loop

    while is_valid:     # Loop until valid input or attempts exhausted

        slow_print("Enter password to access saved passwords: ")
        access_pass = str(input())
        print()  # For better readability

        if access_pass == correct_pass:
            try:
                with open(file_path, "r") as file:
                    content = file.read()
                    slow_print("Saved Passwords:\n")
                    slow_print("-----------------------------\n")
                    print()  # For better readability
                    slow_print(content + "\n")

            except FileNotFoundError:
                slow_print("Error: File path not found. Please check your drive or path.\n")
                print()  # For better readability
            is_valid = False # Exit the loop after successful access
        else:
            chances -= 1
            slow_print(f"Incorrect password! You have {chances} attempts left.\n")
            slow_print("-------------------------------------------------------\n")
            print()  # For better readability
            if chances == 0:
                slow_print("No attempts left! Access denied.\n")
                print()  # For better readability
                is_valid = False # Exit the loop after exhausting attempts
            
            



# Main function to run the password manager           
def main():
    print("------------------------------")
    print("       Password Manager       ")
    print("------------------------------")

    while True:
        slow_print("Choose an option:\n1. Generate Password\n2. Generate Password with Name\n3. Manual Password with Name\n4. Show Saved Passwords\n5. Exit\n")
        print()  # For better readability
        choice = input("Enter your choice (1-5): ").strip()
        print()  # For better readability

        if choice == '1':
            pass_input()
        elif choice == '2':
            pass_name_input()
        elif choice == '3':
            manual_pass_name_input()
        elif choice == '4':
            show_passwords() 
        elif choice == '5':
            slow_print("Exiting Password Manager. Goodbye!\n")
            break
        else:
            slow_print("Invalid choice! Please select a valid option.\n")
            print("----------------------------------------")  # For better readability
            print()
        exit_fnc = input("Do you want to stay? (y/n): ").strip().lower()
        print()  # For better readability

        if exit_fnc.startswith('n'):
            slow_print("Exiting Password Manager. Goodbye!\n")
            break
        else:
            print("----------------------------------------")  # For better readability
            print()

# Run the main function
if __name__ == "__main__":
    main()






