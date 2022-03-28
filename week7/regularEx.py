import re

with open('addresses.txt') as f:
    addresses = f.read()

#all phone no
pattern = re.compile(r'\d{2} \d{2} \d{2} \d{2}')
numbers = pattern.findall(addresses)
#print(numbers)


#All zipCodes
pattern = re.compile(r'(\d{4}) \w+')
zips = pattern.findall(addresses)
#print(zips)

#zip and city name
pattern = re.compile(r'(\d{4}) (\w+)')
zips = pattern.findall(addresses)
#print(zips)

#street Name
pattern = re.compile(r'[a-zA-ZæøåÆØÅ]+ \d+|[a-zA-ZæøåÆØÅ]+ \d')
zips = pattern.findall(addresses)
print(zips)