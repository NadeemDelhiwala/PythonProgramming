# looping in tuples

mixed = (1, 2, 3, 4.0)
print(mixed)

# for loop and tuple
print("Tuple using for loop...")
for i in mixed:
    print(i)
    
print("Tuple using while loop...")
i = 0
while i < len(mixed):
      print(mixed[i]) 
      i += 1

# tuple with one element
nums = (1)
words = ('word')
print(type(nums))  # not a tuple it is an int 
print(type(words))  # not a tuple it is an int 
print(type(mixed))  # it a tuple
wording = ('word#1',)
print(type(wording))  # for storing one element we should use comma after first elem

# tuple without parenthesis
guitar = 'yamaha', 'baton rouge', 'taylor'
print(guitar)
print(type(guitar))

# tuple unpacking
guitarists = ('Maneli Jamal', 'Eddie Van Der Meer', 'Andrew Foy')
guitarists1, guitarists2, guitarists3 = (guitarists)
print(guitarists)
print("--Unpacking tuple into different variable--")
print(guitarists1)
print(guitarists2)
print(guitarists3)
# unpacking -> the number of elem in tuple will always be equal to variables. if we create less # varaiable then it will raise error
print("--------------------------------------------")

# list inside tuple

favorites = ('southern magnolia', ['Tokyo Ghoul Theme', 'Landscape'])
print(favorites)
favorites[1].pop()
print(favorites)
favorites[1].append("we appended")
print(favorites)
# some functions that you can use with tuple
# min
# max
# sum
print("----------------------------------")
print(mixed)
print(min(mixed))
print(max(mixed))
print(sum(mixed))
print("----------------------------------")
