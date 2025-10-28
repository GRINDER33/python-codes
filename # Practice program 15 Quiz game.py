# ractice program 15 Quiz game

questions = (("How many elements are in the periodic table?: "), 
             ("Which animal lays the largest eggs?: "), 
             ("What is the most abundant gas in Earth's atmosphere?: "), 
             ("How many bones does the human body has?: "), 
             ("Which planet in the solar system is the hottest?: "))


options = (("A. 116", "B. 117", "C. 118", "D. 119"), 
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"), 
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C", "D", "A", "A", "B")
guesses =  []
question_num = 0
score = 0

for question in questions:
    print("----------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    while True:
        guess = input("Enter (A, B, C, D): ").upper()
        if guess in ["A", "B", "C", "D"]:
            guesses.append(guess)
            break
        else:
            print("Invalid input!. Please enter a valid option.")
    if guess == answers[question_num]:
        score += 1 
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer!")
    question_num += 1


print("----------------------------------------")
print("                 RESULT                 ")
print("----------------------------------------")

print("Answers; ", end = "")
for answer in answers:
    print(answer, end=" ")
print()
print("Guesses: ", end = "")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score/len(questions) * 100)
print(f"Your score is: {score}%")
