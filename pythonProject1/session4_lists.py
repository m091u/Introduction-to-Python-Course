# errors: 1. first if > instead of < ; 2. elif instead of the second if; 3. second if < instead of > ; input() is a str and not a number but a string

carrots = int(input('How many carrots do you have?'))
rabbits = 6

if rabbits > carrots:
    print('There are not enough carrots')
elif rabbits < carrots:
    print('There are too many carrots')
else:
    print('You have the right number of carrots')


# Lists: written inside square brackets and separated by commas

lottery_numbers = [4, 8, 15, 16, 23, 42]
student_names = ['Diedre', 'Hank', 'Helena', 'Salome']

print(student_names[3])
student_names[0] = 'Bogdan'
print(student_names)

# Exercise 4.1: clothes
clothes = [
"shorts",
"shoes",
"t-shirt",
]

if clothes[0] == "shorts":
    clothes[0] = "warm coat"
print(clothes)


# Functions for lists
costs = [1.2, 4.3, 2.0, 0.5]
print(len(costs))
print(min(costs))
print(max(costs))
print(sorted(costs))
print(list(reversed(costs)))

# Exercise 4.2: game scores
scores = [10, 200, 3, 100, 4, 8, 30, 45, 76, 29]

print(f'Number of scores:{len(scores)}')
print(f'Highest score: {max(scores)}')
print(f'Lowest score: {min(scores)}')
print(sorted(scores))

# append() and in
student_name = input('Which student are you looking for? ')
students = [
'Diedre', 'Hank', 'Helena', 'Salome',
]
if student_name in students:
    print(f'{student_name} is in the class')
else:
    print(f'{student_name} is not in the class')

students = [
'Diedre', 'Hank', 'Helena', 'Salome',
]
student_name = input('What is the name of the new student? ')
students.append(student_name)
print(students)

# Exercise 4.3: shopping list
list = [
    'tomatoes',
    'bread',
    'nuts'
]
if 'bread' in list:
    list.append('butter')
print(list)


fridge = [
    'cheese',
    'pizza',
    'coke',
]

if 'milk' not in fridge:
    print('You have no milk in the fridge')


# For Loops ♥ Lists
student_names = ['Diedre', 'Hank', 'Helena', 'Salome']
count = 0
for student_name in student_names:
    count = count + 1
print(count)


# Exercise 4.4: money spent
costs = [8.30, 7.12, 5.01, 1.00, 0.99, 5.92, 3.50]
total_cost = 0

for cost in costs:
    total_cost = total_cost + cost
print(f'Total cost is {total_cost}')