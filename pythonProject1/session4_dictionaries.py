# Dictionary: Stores a colleciton of labelled items. Each item has a key and a value

person = {
    'name': 'Jessica',
    'age': 23,
    'height': 172
}

print(person['name'])

# Exercise 4.5: Print the values of name , post_code and street_number from the dictionary
place = {
    'name': 'The Anchor',
    'post_code': 'E14 6HY',
    'street_number': '54',
    'location': {
        'longitude': 127,
        'latitude': 63,
    }
}

print(f'The places name is {place['name']}, the postal code is {place['post_code']} and the street number is {place['street_number']}')
print(f'The longitude is {place['location']['longitude']} and the latitude is {place['location']['latitude']}')

# Dictionaries in Lists
people = [
    {'name': 'Jessica', 'age': 23},
    {'name': 'Trisha', 'age': 24},
]
for person in people:
    print(person['name'])
    print(person['age'])

# Exercise 4.6:
fruits = [
    {'name': 'apple', 'colour': 'red', 'price': 0.12},
    {'name': 'banana', 'colour': 'yellow', 'price': 0.2},
    {'name': 'pear', 'colour': 'green', 'price': 0.19},
]

for fruit in fruits:
    print(f'Fruit name is {fruit['name']}, color is {fruit['colour']} and price is {fruit['price']}')

# Random Choice
import random
colours = ['red', 'green', 'blue']
chosen_colour = random.choice(colours)
print(chosen_colour)


# Exercise 4.7: random name
firstnames = ['ana', 'maria', 'sofia', 'clara']
lastnames = ['pop', 'pap', 'pip', 'pep']
chosen_name = random.choice(firstnames) + ' ' + random.choice(lastnames)
print(chosen_name)


verbs = ['sing', 'laugh', 'run']
nouns = ['girls', 'cats', 'kids']
sentence = random.choice(nouns) + ' ' + random.choice(verbs)
print(sentence)


# Question 3 - missing closing ]
trees = [
    {'leaf_colour': 'green', 'height': '2120'},
    {'leaf_colour': 'green', 'height': 2300},]

new_tree = {
'leaf_colour': 'green',
'height': 1020
}

trees.append(new_tree)
print(trees)