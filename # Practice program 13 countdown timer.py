# Practice program 13 countdown timer

import time 

while True:
    try:
        my_time = int(input("Enter the time in seconds: "))

        for x in range(my_time , 0 , -1):
            seconds = x % 60
            minutes = int(x / 60) % 60 
            hours = int(x / 3600)
            print(f"{hours:02}:{minutes:02}:{seconds:02}" ,end="\r")     # \r is a carriage return character   overwrites the previous print
            time.sleep(1)
        print("Times Up!")
        exit_fnc = input("Press q to exit or enter to stay: ")
        if exit_fnc.lower().startswith("q"):
            print("Exiting...")
            break

    except ValueError:
        print("Invalid Input!. Please Re-enter the value!")
 