import random

# Function where the computer chooses with randomly from ['rock', 'paper', 'scissors']
def computer_choice(items_list: list) -> str:
    return random.choice(items_list)

# Function that gets and validates the player's choice
def player_choice() -> str:
    while True:
        player_ipt = input('Please type in (Rock/Paper/Scissors): ').lower()
        if player_ipt not in ['rock', 'paper', 'scissors', 'bye']:
            print('Please type in a valid option or bye for exit!\n')
        else:
            return player_ipt

# Handles game rounds, compares choices, and updates the score
def play_game(scores: dict, player_name: str, rounds: int) -> dict:

    for i in range(1, rounds+1):
        item = ['rock', 'paper', 'scissors']
        computer = computer_choice(item)
        player_input = player_choice()

        if player_input == 'bye':
            print('Exiting the Game...\nBye 👋!!!')
            break

        print(f'Computer chose: {computer.capitalize()} ')
        print(f'{player_name} chose: {player_input.capitalize()}')
        print(f'Round: {i}')


        if computer == 'rock' and player_input == 'scissors':
            print('Computer wins as Rock crushes Scissors')
            scores['Computer'] += 1
        elif computer == 'rock' and player_input == 'paper':
            scores[player_name] += 1
            print(f'{player_name} wins as Paper covers Rock')

        elif computer == 'scissors' and player_input == 'paper':
            scores['Computer'] += 1
            print('Computer wins as Scissors cut Paper')
        elif computer == 'scissors' and player_input == 'rock':
            scores[player_name] += 1
            print(f'{player_name} wins as Rock crushes Scissors')

        elif computer == 'paper' and player_input == 'rock':
            scores['Computer'] += 1
            print('Computer wins as Paper covers Rock')
        elif computer == 'paper' and player_input == 'scissors':
            scores[player_name] += 1
            print(f'{player_name} wins as Scissors cut Paper')

        elif computer == player_input:
               print('It\'s a draw')
        print()

    print(f"Final scores:\nComputer = {scores['Computer']} | {player_name}: {scores[player_name]}\n")
    return scores

# Determines the final winner based on the scores
def winner_loser(score_board, name):
    if score_board['Computer'] > score_board[name]:
        return f'The winner is Computer!💻🎉💻 \n'
    elif score_board['Computer'] < score_board[name]:
        return f'The winner is {name}! 🎉 🎉 🎉 \n'
    else:
        return 'It\'s a tie 🤝!\n'

# Main function to start the game, ask for player info, and handle replay
def main():

    print('Welcome to Rock-Paper-Scissors!!! You\'ll have 10 attempts to beat the computer!!!\n')

    while True:
        player_name = input('Please enter your name: ')
        print()
        score_board = {'Computer': 0, player_name: 0}

        try:
            round_number = int(input('How many rounds do you like to play?: '))
        except ValueError:
            print(f'Invalid input. Defaulting to 1 round.')
            round_number = 1

        result = play_game(score_board, player_name, round_number)
        print(winner_loser(result, player_name))

        game = input('Do you want to play again (Y/N): ').lower()

        if game in ['no', 'n']:
            print('Hope to see you again!!! 👋')
            break

if __name__ == '__main__':
    main()