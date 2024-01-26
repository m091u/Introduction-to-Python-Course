# exercise 2.1 usage of input()
city = input('What city do you live in?')
country = input('Which country do you come from?')

print('You live in {} and come from {}'.format(city, country))

# int()
purchased_apples = input('How many apples did you buy? ')
print(type(purchased_apples))
total_apples = int(purchased_apples) + 5
print(total_apples)


#Exercise 2.2 Write a program calculate how many pizzas you need to feed you and your friends
friends = input('How many friends are coming over?')
pizzas = int(friends)* 0.5

print('You need {} pizzas for {} friends'. format( pizzas, friends))

