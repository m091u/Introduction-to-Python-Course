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

