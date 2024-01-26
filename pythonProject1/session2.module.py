# Module: Code that someone else has written that you can reuse in your programs

import datetime

x = datetime.datetime.now()
print(x)

my_date = datetime.date(2024,1,30)
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