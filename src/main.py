import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
        valid_choices = ["rock", "paper", "scissors", "Rock", "Paper", "Scissors"]
        if user_choice.lower() in [choice.lower() for choice in valid_choices]:
            return user_choice.lower()
        else:
            print("eso no se vale")

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        play_again = input("\nPlay again? (yes/no): ")
        if play_again.lower() in ["no", "n"]:
            break
        elif play_again.lower() not in ["yes", "y"]:
            print("Please enter yes or no")
            continue

if __name__ == "__main__":
    play_game()
