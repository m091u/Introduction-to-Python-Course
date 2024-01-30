print("foo", 42, "bar")

print("foo", 42, "bar", sep="/")  #adding a separator

d = {"foo": 1, "bar": 2, "baz": 3}
for k, v in d.items():
    print(k, v, sep=" -> ")

for number in range(10):
    print(number, end=(" " if number < 9 else "\n"))


# name = input("What is your name? ")
# age = input('what is your age')
# print(f"Hello, {name}. You are {age}.")

# for loops
a = ['foo', 'bar', 'baz']
for i in a:
    print(i+'and')

print(iter('foobar'))

itr = iter(a)
print(set(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))

# iterating through a dictionary
d = {'foo': 1, 'bar': 2, 'baz': 3}
for k in d:
    print(f'printing {k} and {d[k]}')

# iterate through a dictionary accessing values
for v in d.values():
    print(f'printing values {v} only')

# iterate through a dictionary accessing both the keys and values
for k, v in d.items():
    print(f'printing both key {k} and value {v}')

# iterating through a range
x = range(5)
print(tuple(x))

for i in x:
    print(i)

# range(<begin>, <end>, <stride>) returns an iterable that yields integers starting with <begin>, up to but not including <end>.
# If specified, <stride> indicates an amount to skip between values
f = list(range(5, 20, 3))

print(f)

for i in ['foo', 'bar', 'baz', 'qux']:
    if 'x' in i:
        break
    print(i)


for i in ['foo', 'bar', 'baz', 'qux']:
    if i == 'bal':
       break
    print(f'iteration with break {i}')
else:
    print('Done.')


# functions
def hello():
    name = str(input("Enter your name:"))
    if name:
        print(f'Hello {name}')
    else:
        print('Hello world')
    return

hello()

# lambada functions
# Define a lambda function that adds two numbers
add_numbers = lambda x, y: x + y

# Use the lambda function
result = add_numbers(5, 3)

# Print the result
print("Result of adding two numbers:", result)

# example 2
numbers = [1, 2, 3, 4, 5]

# Use a lambda function with map to square each number
squared_numbers = list(map(lambda x: x**2, numbers))


print("Original Numbers:", numbers)
print("Squared Numbers:", squared_numbers)