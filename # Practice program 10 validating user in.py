# Practice program 10 validating user input
# 1. username is not more than 12 characters
# 2. username must not contain spaces
# 3. usename must nor contain digits

username = input("Ente a username: ")

if len(username) > 12:
    print("Your username cant be more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username cant contain spaces")
elif username.isdigit():
    print("Your username cannot contain digits")
else:
    print(f"Welcome {username}")