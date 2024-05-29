import random
import time

def generate_sequence(difficulty):
    sequence = []
    for i in range(difficulty):
        sequence.append(random.randint(1, 101))
    return sequence

def get_list_from_user(difficulty):
    user_list = []
    for i in range(difficulty):
        user_list.append(int(input(f"Enter number {i+1}: ")))
    return user_list

def is_list_equal(generated_sequence, user_sequence):
    return generated_sequence == user_sequence

def play_memory_game(difficulty):
    generated_sequence = generate_sequence(difficulty)
    print(f"Remember this sequence: {generated_sequence}")
    time.sleep(0.7)
    user_sequence = get_list_from_user(difficulty)
    if is_list_equal(generated_sequence, user_sequence):
        print("Good Job!")
        return True
    else:
        print(f"Sorry, Not good {generated_sequence}.")
        return False
