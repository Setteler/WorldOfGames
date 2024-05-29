import random
import requests

def get_exchange_rate():
    response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
    data = response.json()
    return data["rates"]["ILS"]

def get_money_interval(usd_amount, exchange_rate, difficulty):
    interval_range = 5 - difficulty
    value_in_ils = usd_amount * exchange_rate
    return (value_in_ils - interval_range, value_in_ils + interval_range)

def get_guess_from_user(usd_amount):
    return float(input(f"Guess the value of {usd_amount} USD in ILS: "))

def play(difficulty):
    usd_amount = random.randint(1, 100)
    exchange_rate = get_exchange_rate()
    interval = get_money_interval(usd_amount, exchange_rate, difficulty)
    user_guess = get_guess_from_user(usd_amount)
    if interval[0] <= user_guess <= interval[1]:
        print("Congratulations!")
        return True
    else:
        print(f"Sorry {interval[0]:.2f} and {interval[1]:.2f}.")
        return False
