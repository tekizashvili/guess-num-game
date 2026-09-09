import random

WELCOME_TEXT = "Welcome to the Number Guessing Game!\n" \
    "I'm thinking of a number between 1 and 100."
    
DIFFICULTY_INTRUCTION = "Please select the difficulty level:\n" \
    "1. Easy (10 chances)\n" \
    "2. Medium (5 chances)\n" \
    "3. Hard (3 chances)\n"
    
RANDOM_NUMBER = random.randint(1, 100)

def choose_difficulty() -> str:
    print(DIFFICULTY_INTRUCTION)
    while True:
        user_input = input("Enter your choice: ")
        if user_input not in ['1', '2', '3']:
            print("\nInvalid input. Please choose '1', '2' or '3'.\n")
        else:
            break
    
    if user_input == '1':
        return ('Easy', 10)
    elif user_input == '2':
        return ('Medium', 5)
    else:
        return ('Hard', 3)

def play_game() -> None:
    attempt_count = 0
    difficulty = choose_difficulty()
    
    print(f"\nGreat! You have selected the {difficulty[0]} difficulty level.\n" \
            f"You have {difficulty[1]} chances to guess the correct number.\n" \
            "Let's start the game!"
    )
    
    while True:
        if attempt_count >= difficulty[1]:
            print('\nSorry, you have run out of attempts.')
            break
        player_guess = input('\nEnter your guess: ')
        if player_guess.isdigit():
            attempt_count += 1
            if int(player_guess) > RANDOM_NUMBER:
                print(f"Incorrect! The number is less than {player_guess}")
            elif int(player_guess) < RANDOM_NUMBER:
                print(f"Incorrect! The number is greater than {player_guess}")
            else:
                print(f"Congratulations! You guessed the correct number in {attempt_count} attempts.")
                break
        else:
            print("Please, choose a positive integer.")


def game() -> None:
    while True:
        play_game()
        
        while True:
            user_decision = input("\nDo you want to play the game again? Press Y/N ")
            print()
            if user_decision.lower() in ('y', 'n'):
                break
            else:
                print("Please type and submit N or Y.")
        
        if user_decision == 'n':
            break
                
                
def main():
    print(WELCOME_TEXT, "\n")
    
    game()


if __name__ == "__main__":
    main()