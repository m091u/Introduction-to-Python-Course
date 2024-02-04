import random

for number in range(9):
    print('~' * number)

today = input('What day is today?')
is_monday = today == 'monday'

print(f'Today is monday : {is_monday}')

# float() - converts strongs into floats

temp = input('What is the temperature?')
is_freezing = float(temp) <=0.0
print(f'Temperature is freezing: {is_freezing}')

# Exercise 1

price = input('What is the price of a burger?')
in_budget = float(price) <= 10.00
print(f'Burger is within budget: {in_budget}')

vegetarian = input('Do they have veg options? y/n')
has_veg = vegetarian == 'y'
meets_criteria = in_budget and has_veg
print(f'Restaurant meets criteria: {meets_criteria}')

# visit Mars

mars_choice = input('Would you like to visit Mars? y/n')
is_willing = mars_choice == 'y'

affordable = input('Can you afford it? y/n')
can_afford = affordable == 'y'

should_visit_mars = is_willing and can_afford

print(f'You should visit mars: {should_visit_mars}')

# if statement
name = input("What is your name? ")
is_admin = name == 'admin'

password = input("What is your password? ")
is_correct = password == 'parola'

if is_admin and is_correct:
    print('Welcome!')

if not is_admin or not is_correct:
    print('Go away')


price = input('What is the price of a burger?')
in_budget = float(price) <= 10.00

vegetarian = input('Do they have veg options? y/n')
has_veg = vegetarian == 'y'

if in_budget and has_veg:
    print('This restaurant is a great choice!')
if not in_budget or not has_veg:
    print('Not a good idea')

#  if/ else
name = input("What is your name? ")
is_admin = name == 'admin'
password = input("What is your password? ")
is_password_correct = password == 'dinosaurs'

if is_admin and is_password_correct:
    print('Welcome')
else:
    print('go away')


# Exercise 3.4:
meal_price = float(input('How much did the meal cost? '))
discount_choice = input('Do you have a discount? y/n ')

is_discount = discount_choice == 'y'
is_over_twenty = meal_price >= 20.0
discount_applicable = is_discount and is_over_twenty

if discount_applicable:
    meal_price = meal_price*0.9
    print('Discount applied')
else:
    print('No discount')
print(f'Total cost: {meal_price}')

# Exercise 3.5

temp = int(input('What is the ovem temperature?'))

if temp > 200:
    print("The oven is too hot")
elif temp < 150:
    print("The oven is too cold")
elif temp == 180:
    print("The oven is at the perfect temperature")
else:
    print("The temperature is close enough")


random_integer = random.randint(1, 100)
print(random_integer)


sides = int(input('How many sides does the dice have? '))
random_integer = random.randint(1,  sides)

print(f'Your rolled a {random_integer}')

print(True and True)
print(True and False)
print(True or True)
print(True or False)