# Module: Code that someone else has written that you can reuse in your programs

import datetime

x = datetime.datetime.now()
print(x)

my_date = datetime.date(2024, 1, 30)
print(my_date.strftime("%d-%b-%Y"))

# for loop
for number in range(5):
    print("executing FOR LOOP - run No {}".format(number + 1))

for character in 'Banana':
    print(character)

for character in 'Banana':
    print('<' + character + '>')

for name in ['Mary', 'Ranjit', 'Fatima']:
    print(name)

total = 0
for number in range(3):
    print("This is loop execution for digit: " + str(number) + " inside the loop \n")
    total = total + 1  # every time the loop executes, we add 1 to the total

print("The final TOTAL value is: " + str(total))

# while loop
store_capacity = 5

while store_capacity > 0:
    print('Please come in. Spaces available:' + str(store_capacity))
    store_capacity = store_capacity-1
print('\nPlease wait for someone to exit.')

# Functions


def hello():
    print('hello world!')


hello()

# Pass single argument to a function


def hello_again(person_name):
    print('Hello,', person_name)


hello_again('Maria')
hello_again('Kim')
hello_again('Olya')

# Pass multiple arguments
# positional arguments


def some_function(person_name, job):
    print(person_name, 'is a', job)


some_function('Fiona', 'developer')

# keyword arguments: in this case, the order of the arguments no longer matters


def some_function(person_name, job):
    print(person_name, 'is a', job)


some_function(job='developer', person_name='Fiona')
some_function(person_name='Fiona', job='judge')

# Default Arguments


def some_function(person_name, job='doctor'):
    print(person_name, 'is a', job)


some_function('Fiona')
some_function('Fiona', 'manager')

# Returning Values from Function


def calculate_sum(a, b):
    return a + b


result = calculate_sum(10, 15)
print(f'result is: {result}')


def circle_area(radius):
    area = 3.14 * (radius**2)
    return area


print(circle_area(9))


def days_in_hours(days):
    hours = days * 24
    return hours


print(days_in_hours(5))


def times_two(num):
    result = num * 2
    return result


for number in range(4):
    calc_res = times_two(number)
    print(calc_res)


# Homework



