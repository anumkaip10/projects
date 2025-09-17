import random

print("Let's play Rock, Paper, Scissors!")
print("Enter your choices: (1) Rock  (2) Paper  (3) Scissors!")

user_choice = int(input("Your choice (1-3): "))
computer_choice = random.randint(1, 3)
choices = ("Rock", "Paper", "Scissors")

print(f"You chose: {choices[user_choice-1]}")
print(f"Computer chose: {choices[computer_choice-1]}")

if user_choice == computer_choice:
    print("It's a Tie!")
elif (user_choice == 1 and computer_choice == 3) or \
     (user_choice == 2 and computer_choice == 1) or \
     (user_choice == 3 and computer_choice == 2):
    print("You win!")
else:
    print("Computer wins!")
