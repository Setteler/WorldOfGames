from Live import welcome, load_game
import GuessGame
import MemoryGame
import CurrencyRouletteGame



name = input("Please enter your name: ")
print(welcome(name))

game_number, game_level = load_game()
if game_number == 1:
    MemoryGame.play_memory_game(game_level)
elif game_number == 2:
    GuessGame.play_guess_game(game_level)
elif game_number == 3:
    CurrencyRouletteGame.play(game_level)

