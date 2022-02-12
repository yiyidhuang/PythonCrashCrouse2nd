import random

jackpot = list(range(10)) + ['a', 'l', 'o', 't', 'n']
winning_number = random.sample(jackpot, k=4)
print(f"If your number is {winning_number}, the congrats! you win the lottery")
