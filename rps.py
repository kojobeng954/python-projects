import random


def play_game():
    choice = ["rock", "paper", "scissors"]
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    computer_choice = random.choice(choice)

    if user_choice not in choice:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        return
    elif user_choice == computer_choice:
        print(f"Both players selected {user_choice}. It's a tie!")
    elif user_choice == "rock" and computer_choice == "paper":
        print("Paper beats rock! You win!")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("Rock beats scissors! You win!")
    elif user_choice == "paper" and computer_choice == "rock":
        print("Paper beats rock! You win!")
    elif user_choice == "paper" and computer_choice == "scissors":
        print("Scissors beats paper! You lose!")
    elif user_choice == "scissors" and computer_choice == "rock":
        print("Rock beats scissors! You lose!")
    elif user_choice == "scissors" and computer_choice == "paper":
        print("Scissors beats paper! You win!")


play_game()
