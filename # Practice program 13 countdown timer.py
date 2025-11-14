# Practice program 13 countdown timer

import time 
import winsound

def slow_print(text, delay=0.01):
    for letter in text:
        print(letter, end="", flush=True)
        time.sleep(delay)


while True:
    try:
        ## Hours
        slow_print("Enter hours: ")
        time_hour_input = input()
        if time_hour_input.strip() == "":
            time_hour = 0
        else:
            time_hour = int(time_hour_input)
            if time_hour < 0:
                raise ValueError()

        ## Minutes
        slow_print("Enter minutes: ")
        time_minutes_input = input()          
        if time_minutes_input.strip() == "":
            time_minutes = 0
        elif int(time_minutes_input) > 60:
            print("Minutes should be less than 60")
            continue
        else:  
            time_minutes = int(time_minutes_input)

            if time_minutes < 0:
                raise ValueError()

        ## Seconds
        slow_print("Enter seconds: ")
        time_seconds_input = input()
        if time_seconds_input.strip() == "":
            time_seconds = 0
        elif int(time_seconds_input) > 60:
            print("Seconds should be less than 60")
            continue
        else:  
            time_seconds = int(time_seconds_input)

            if time_seconds < 0:
                raise ValueError()

        my_time = time_hour * 3600 + time_minutes * 60 + time_seconds

                
        print()
        slow_print(f"Timer set for {time_hour} hours, {time_minutes} minutes and {time_seconds} seconds.")
        print()
   
        for x in range(my_time , 0 , -1):
            seconds = x % 60
            minutes = int(x / 60) % 60 
            hours = int(x / 3600)
            print(f"{hours:02}:{minutes:02}:{seconds:02}", end = "\r")     # \r is a carriage return character   overwrites the previous print
            time.sleep(1)
        print("Times Up!")

        sound = winsound.PlaySound("yo_phone_linging.wav", winsound.SND_FILENAME)
      
        exit_fnc = input("Press q to exit or enter to stay: ")
        if exit_fnc.lower().startswith("q"):
            print("Exiting...")
            break

    except ValueError:
        print("Invalid Input!. Please Re-enter the value!")
 