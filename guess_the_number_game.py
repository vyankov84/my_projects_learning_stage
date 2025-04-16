import random

# Handles the game logic and difficulty mode selection
def play_game():
    print("Welcome to guess the number game!")
    print()
    print("There are 3 modes:\n1.Easy: 10 attempts\n2.Normal: 7 attempts\n3.Hard: 5 attempts\n4.Exit")

    while True:
        try:
            choice = input("Enter mode: ")
            if choice == '1':
                num_range = 10
                break
            elif choice == '2':
                num_range = 7
                break
            elif choice == '3':
                num_range = 5
                break
            elif choice == '4':
                print("Exiting game. Goodbye!")
                exit()
            else:
                print('Incorrect choice! Try again!')
        except ValueError:
            print("Invalid input! Please enter number (1-4)")

    value = random.randint(1, 100)
    is_guessed = False

    for i in range(1, num_range + 1):

        # Check if the input is valid number between 1 and 100
        try:
            guess_number = int(input(f"Attempt {i}: "))

            if not (1 <= guess_number <= 100):
                print("Your guess should be between 1 and 100")
            elif guess_number > value:
                print("The number is lower")
            elif guess_number < value:
                print("The number is higher")
            else:
                print(f"Congratulations you win!!! The number is {value} and you found it from {i} attempts.")
                is_guessed = True
                break
        except ValueError:
            print("Invalid input! Please enter number between (1-100)")
    # Display the correct number if the player didn't guess it
    if not is_guessed:
        print(f"Sorry, you didn't guess the number! It was {value}.")

# Main function to start the game and handle replay
def main():
    while True:
        play_game()
        print()
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again == "n":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()