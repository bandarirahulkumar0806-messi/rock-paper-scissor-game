import random

print("----- Welcome to Rock-Paper-Scissors Game -----")
print("Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock")
print("------------------------------------------------\n")

# Score tracking
user_score = 0
computer_score = 0

# Game loop
while True:
    # User input
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please choose rock, paper, or scissors.\n")
        continue

    # Computer random choice
    computer_choice = random.choice(["rock", "paper", "scissors"])
    
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    # Game logic
    if user_choice == computer_choice:
        print("It's a Tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("✅ You Win this round!")
        user_score += 1
    else:
        print("❌ You Lose this round!")
        computer_score += 1

    # Show scores
    print(f"Score => You: {user_score} | Computer: {computer_score}\n")

    # Play again option
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("\nFinal Score => You:", user_score, "| Computer:", computer_score)
        print("🎮 Thanks for playing Rock-Paper-Scissors!")
        break
