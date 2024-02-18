# Question 1
# Create a program that tells you if you need an umbrella when you leave the house.

is_raining = input('Is it raining? y/n')
if is_raining == 'y':
    print("Take an umbrella")
elif is_raining == 'n':
    print("You don't need an umbrella")
else:
    print('Check your answer')

# Question 2

my_money = int(input('How much money do you have? '))
boat_cost = int(20 + 5)
if my_money >= boat_cost:
    print('You can afford the boat hire')
else:
    print('You cannot afford the board hire')


# Question 3
year = int(input('What is the year of the book?'))

if 1800 < year < 1900:
    century = "Nineteenth"
elif 1900 <= year < 2000:
    century = "Twentieth"
elif year == 1800:
    century = "Eighteenth"

decade_number = int(year % 100 / 10)
if decade_number == 0:
    decade = "Noughties"
elif decade_number == 1:
    decade = "Tens"
elif decade_number == 2:
    decade = "Twenties"
elif decade_number == 3:
    decade = "Thirties"
elif decade_number == 4:
    decade = "Forties"
elif decade_number == 5:
    decade = "Fifties"
elif decade_number == 6:
    decade = "Sixties"
elif decade_number == 7:
    decade = "Seventies"
elif decade_number == 8:
    decade = "Eighties"
elif decade_number == 9:
    decade = "Nineties"
else:
    decade = "Unknown Decade"

if 1800 < year < 1950:
    print(f'Your book is from the {century} century and the {decade}')
else:
    print('Year is incorrect')


# Extra Exercise 2 Word Jumble Game
import random
words =['cat', 'rain', 'pear', 'apple', 'banana', 'orange', 'strawberry', 'peach']

word = random.choice(words)
jumbled_word = ''.join(random.sample(word, len(word)))
print(f'The jumbled word is: {jumbled_word}')

guess = input("Guess the original word: ")

if guess == word:
    print('You guessed')
else:
    print('That is incorrect. The word was:', word)
