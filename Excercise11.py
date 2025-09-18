# create a program able of displaying questions to user like KBC.

questions = [
    "Q1: What is the capital of Pakistan?",
    "Q2: Who is the founder of Pakistan?",
    "Q3: Which is the national animal of Pakistan?"
]

options = [
    ["A. Karachi", "B. Lahore", "C. Islamabad", "D. Quetta"],
    ["A. Allama Iqbal", "B. Liaquat Ali Khan", "C. Quaid-e-Azam", "D. Sir Syed Ahmed Khan"],
    ["A. Markhor", "B. Lion", "C. Tiger", "D. Elephant"]
]

answers = ["C", "C", "A"]  # Correct options

score = 0

for i in range(len(questions)):
    print(questions[i])
    for opt in options[i]:
        print(opt)

    user_ans = input("Enter your answer (A/B/C/D): ").upper()

    if user_ans == answers[i]:
        print(" Correct!\n")
        score += 1
    else:
        print(f" Wrong! Correct answer is {answers[i]}\n")

print(f" Your Final Score: {score}/{len(questions)}")

