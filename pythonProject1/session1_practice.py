# py data types
cats = 10
cans = 2
total_cans = cats * cans
print(total_cans)
# output = str(cats) + " cats eat " + str(total_cans) + " cans"
output = "{} cats eat {} cans".format(cats, total_cans)
print(output)

# Extension solution
cats = 10
cans = 2
days = 7
total_cans = cats * cans * days
print(total_cans)
# msg = "{} cats eat {} cans in {} days".format(cats, total_cans, days)
msg = f'{cats} cats eat {total_cans} cans in {days} days'
print(msg)

# additional material

print(ord('c'))
print(chr(87))

# slicing
s = 'sunny'
print(s[1:4])
print(s[:4] + s[4:])
print(s[::2])   #with a second :(stride) every x character is skipped

num = '12345' * 5
print(num)
print(num[::5])

# reverse a string
quote = 'If Comrade Napoleon says it, it must be right.'
print(quote[::-1].title())

# Interpolating Variables Into a String - f-string
n = 20
m = 25
prod = n * m
print(f'The product of {n} and {m} is {prod}')

s = 'mirabela'
s = s.replace('l', 'll')
print(s.upper())

s = 'foo'
t = 'bar'
print('barf' in 2 * (s + t))


str = 'foobar'
print(str[::-5])
print(str[::-1][::-5])
print(str[::5])
print(str[::-1][-1] + s[len(s)-1])
print(str[0] + s[-1])
