# intro
print('Hello, Mira!')
print('How are you?')
print()
print(5 - 6)
print(8 * 9)
print(6 / 2)
print(5.0 / 2)
print(5 % 2)
print(2 * (10 + 3))
print(2 ** 4)

print("Cat" * 3)
print("Cat" + str(3))
print("Cat".upper())
print("Cat".lower())
print("the lord of the rings".title())

# variables
oranges = 12
cost_per_orange = 0.5

total_cost = oranges * cost_per_orange
print(str(oranges) + " oranges")
print("costs " + str(total_cost))

# recap
days = 31
hours = "24"
total_hours = days * hours
msg = "There are {} in {} days".format(total_hours, days)
print(msg)

# String Formatting
oranges = 12
cost_per_orange = 0.5
total_cost = oranges * cost_per_orange
output = "{} oranges costs £{}".format(oranges, total_cost)
print(output)

# homework
my_name = "Penelope"
my_age = 29
message = 'My name is {} and I am {} years old'.format(my_name, my_age)