import random

def get_user_choice():
    print("Choose one:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    
    while True:
        try:
            user_choice = int(input("Enter the number of your choice (1-3): "))
            if user_choice in [1, 2, 3]:
                return user_choice
            else:
                print("Incorrect input. Please choose 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_computer_choice():
    return random.randint(1, 3)

def determine_winner(user_choice, computer_choice):
    choices = ["Rock", "Paper", "Scissors"]
    print(f"\nYou chose: {choices[user_choice - 1]}")
    print(f"Computer chose: {choices[computer_choice - 1]}")
    
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 3 and computer_choice == 2):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    print("Welcome to Rock, Paper, Scissors!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    main()
