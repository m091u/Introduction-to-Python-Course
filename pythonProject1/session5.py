animals = [
{'species': 'zebra', 'name': 'Penelope'},
{'species': 'penguin', 'name': 'Jenn'},
{'species': 'elephant', 'name': 'Harris'},
{'species': 'flamingo', 'name': 'Florence'},
]

for animal in animals:
    print(animal['species'])

# TXT files
with open('people.txt', 'w+') as text_file:
    people = 'Joanne \nSusan \nAmina'
    text_file.write(people)

with open('people.txt', 'w+') as text_file:
    people = 'Joanne \nSusan \nAmina'
    text_file.write(people)

# Exercise 5.1: Create a to-do list program that writes user input to a file

new_item = input('Enter a to-do item: ')
with open('todo.txt', 'r') as todo_file:
    todo = todo_file.read()

todo = todo + new_item + '\n'

with open('todo.txt', 'w+') as todo_file:
    todo_file.write(todo)


# CSV files
import csv
field_names = ['name', 'age']
data = [
    {'name': 'Jill', 'age': 32},
    {'name': 'Sara', 'age': 28},
]
with open('team.csv', 'w+') as csv_file:
    spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names)
    spreadsheet.writeheader()
    spreadsheet.writerows(data)

# Reading a CSV
import csv
with open('team.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    for row in spreadsheet:
        print(dict(row))


# Exercise 5.2: Shortest tree
import csv
with open('trees.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)

    heights = []

    for row in spreadsheet:
        tree_height = row['height']
        heights.append(tree_height)

shortest_height = min(heights)
print(shortest_height)




