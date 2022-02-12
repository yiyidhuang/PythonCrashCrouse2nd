import random

jackpot = list(range(10)) + ['a', 'l', 'o', 't', 'n']

n = 1
while True:
    winning_number = random.sample(jackpot, k=4)
    print(f"If your number is {winning_number}, then congrats! you win the lottery")
    my_ticket = random.choices(jackpot, k=4)
    if winning_number != my_ticket:
        n += 1
        continue
    else:
        print(f"It takes you {n} times to win the lottery")
        break

