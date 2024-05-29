def welcome(name):
    return (f'''Hello {name} and welcome to the World of Games (WoG)
Here you can find many cool games to play''')

def load_game():
    from MemoryGame import play_memory_game
    from GuessGame import play_guess_game
    from CurrencyRouletteGame import play as play_currency_roulette
    import Score  # Importing the add_score function

    print('''Please choose a game to play:
        1. Memory Game - a sequence of numbers will appear for 1 second and you have to
        guess it back
        2. Guess Game - guess a number and see if you chose like the computer
        3. Currency Roulette - try and guess the value of a random amount of USD in ILS''')

    while True:
        try:
            game_number = int(input('Enter the game number (1, 2, or 3): '))
            if game_number in [1, 2, 3]:
                break
            else:
                print('Enter a number between 1-3')
        except ValueError:
            print('Enter a valid number')

    while True:
        try:
            game_level = int(input('Enter the game level (1, 2, 3, 4 or 5): '))
            if game_level in [1, 2, 3, 4, 5]:
                break
            else:
                print('Enter a number between 1-5')
        except ValueError:
            print('Enter a valid number')

    if game_number == 1:
        won = play_memory_game(game_level)
    elif game_number == 2:
        won = play_guess_game(game_level)
    elif game_number == 3:
        won = play_currency_roulette(game_level)

    if won:
        Score.add_score(game_level)

    return game_number, game_level
