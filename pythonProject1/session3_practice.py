# python-operators-expressions
def is_divisible(a, b):
    return b != 0 and a % b == 0

print(is_divisible(4, 3))

# the Ternary Operator
day = input('What is the day?')
open_time = '11AM' if day =="sunday" else "9AM"
print(f'Open time is  {open_time}')


# Membership Operators
print(5 not in [2, 3, 5, 9, 7])

print("a" in "cat")

# The Walrus Operator (:=)
def validate_length(string):
    if(n := len(string)) <8:
        print(f"Length {n} is too short, needs at least 8")
    else:
        print(f"Length {n} is okay!")

validate_length("Mirabela")


# if/else/elif
name = 'Joe'
if name == 'Fred':
    print('Hello Fred')
elif name == 'Xander':
    print('Hello Xander')
elif name == 'Joe':
    print('Hello Joe')
elif name == 'Arnold':
    print('Hello Arnold')
else:
    print("I don't know who you are!")

# alternative with dictionary
# dict.get() searches a dictionary for the specified key and returns the associated value if it is found, or the given default value if it isn’t.
names = {
    'Fred': 'Hello Fred',
    'Xander': 'Hello Xander',
    'Joe': 'Hello Joe',
    'Arnold': 'Hello Arnold'
}

print(names.get('Joe', "I don't know who you are!"))


if 'f' in 'foo': print('1'); print('2'); print('3')

raining = False
print("Let's go to the", 'beach' if not raining else 'library')

raining = True
print("Let's go to the", 'beach' if not raining else 'library')
