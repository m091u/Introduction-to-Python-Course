# Question 1: index starts at 0
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
lottery_ticket = [8, 15, 25, 39, 46, 28, 19]
lottery_numbers = random.choice()