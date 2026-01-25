fruits = ['apple', 'banana', 'cherry', 'date']
print(fruits[1]) # output Apple
print(fruits[-1]) # output date

# second excerise
fruits.append("elderberry")
fruits.insert(1,"blueberry")
print(fruits)

# Third excerise
fruits.remove('banana')
del fruits[0]
print(fruits)

# Fourth excerise Slicing Lists
print(fruits[1:3]) # output ['cherry', 'date']