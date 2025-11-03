import random

print(" Welcome to Snake Water Gun Game! ")
print("Rules: Snake  drinks Water  | Gun  kills Snake  | Water 💦 drowns Gun 🔫")

choices = ["snake", "water", "gun"]

while True:
    user_choice = input("\nChoose one (snake / water / gun): ").lower()
    if user_choice not in choices:
        print(" Invalid choice! Try again.")
        continue

    comp_choice = random.choice(choices)
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {comp_choice}")

    # game logic
    if user_choice == comp_choice:
        print(" It's a tie!")
    elif (user_choice == "snake" and comp_choice == "water") or \
         (user_choice == "water" and comp_choice == "gun") or \
         (user_choice == "gun" and comp_choice == "snake"):
        print(" You win!! ")
    else:
        print(" You lose! ")

    play_again = input("\nWanna play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! Come back for revenge ")
        break
