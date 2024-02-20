# Question 1: mistake-> wrong index, for the first item index is 0
import random

shopping_list = [
    "oranges",
    "cat food",
    "sponge cake",
    "long-grain rice",
    "cheese board",
]
print(shopping_list[0])

# Question 2
chocolates = {
    'white': 1.50,
    'milk': 1.20,
    'dark': 1.80,
    'vegan': 2.00,
}

customer_choice = input(' Which chocolate would you like? white/ milk/ dark/ vegan').lower()
if customer_choice in chocolates:
    print(f'The price of {customer_choice} is {chocolates[customer_choice]}')
else:
    print('Sorry, we do not have that chocolate.')

# Question 3 lottery
your_lottery_ticket = [8, 15, 25, 39, 46, 28, 19]
lottery_numbers = [random.choice(range(1, 50)) for _ in range(7)]

matches = 0

for number in your_lottery_ticket:
    if number in lottery_numbers:
        matches += 1

if matches == 3:
    prize = 20
elif matches == 4:
    prize = 40
elif matches == 5:
    prize = 100
elif matches == 6:
    prize = 10000
elif matches == 7:
    prize = 1000000
else:
    prize = 0

print(f"Your lottery numbers: {your_lottery_ticket}")
print(f"Draw numbers: {lottery_numbers}")
print(f"Matching numbers: {matches} and prize: £{prize}")