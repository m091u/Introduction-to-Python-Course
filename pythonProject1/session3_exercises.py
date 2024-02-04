# Exercise 3.6: This program uses random to simulate a coin

import random

def flip_coin():
    random_number = random.randint(1, 2)
    if random_number == 1:
        side = 'heads'
    else:
        side = 'tails'
    return side


choice = input('heads or tails?')
result = flip_coin()

print(f'the coin landed on {result}')
if result == choice:
    print('you won!')
else:
    print('not your lucky day')


# Exercise 3.7: This program simulates rock, paper, scissors.
def random_choice():
    choice_number = random.randint(1, 3)

    if choice_number == 1:
        choice = 'rock'
    elif choice_number == 2:
        choice = 'scissors'
    else:
        choice = 'paper'

    return choice


my_choice = input('Choose rock, scissors or paper: ')
opponent_choice = random_choice()
print(f'Opponent choice is : {opponent_choice}')

if my_choice == 'rock' and opponent_choice == 'scissors':
    print('I win')
elif my_choice == 'rock' and opponent_choice == 'paper':
    print('Opponent wins')
elif my_choice == 'paper' and opponent_choice == 'rock':
    print('I win')
elif my_choice == 'paper' and opponent_choice == 'scissors':
    print('Opponent wins')
elif my_choice == 'scissors' and opponent_choice == 'rock':
    print('Opponent wins')
elif my_choice == 'scissors' and opponent_choice == 'paper':
    print('I win')
elif my_choice == opponent_choice:
    print('Tie')
else:
    print('Chose from available options')


# Exercise 3.8: Not Quite Roulette
your_amount = input(' What amount do you want to bet?')
your_colour = input('Choose a color between red and black')
your_number = int(input('Choose a number between 1 and 100'))


def colour():
    random_number = random.randint(1, 2)
    if random_number == 1:
        colour = 'red'
    else:
        colour = 'black'
    return colour


random_number = random.randint(1, 100)
random_color = colour()
print(random_number, random_color)

if random_color == your_colour:
    your_amount = your_amount
elif random_number == your_number:
    your_amount = your_amount * 2
elif random_color == your_colour and random_number == your_number:
    your_amount = your_amount * 100
else:
    your_amount = 0
print(f'Your amount is {your_amount}')