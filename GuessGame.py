import random

def generate_number(difficulty):
    return random.randint(1, difficulty)

def get_guess_from_user(difficulty):
    return int(input(f"Please guess a number between 1 and {difficulty}: "))

def compare_results(secret_number, user_guess):
    return user_guess == secret_number

def play_guess_game(difficulty):
    secret_number = generate_number(difficulty)
    user_guess = get_guess_from_user(difficulty)
    if compare_results(secret_number, user_guess):
        print("Correct number!")
        return True
    else:
        print(f"Incorrect, number was {secret_number}.")
        return False

