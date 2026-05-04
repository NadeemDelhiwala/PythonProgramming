# generate list with range function

numbers = list(range(1, 11))
print(numbers)

# more about pop method

poped_val = numbers.pop()
print(poped_val)
print(numbers)

# index method

print("Accessing the index position of a given element..")
print(numbers.index(2))

numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 55, 11, 31, 3, 1, 3]
# search second occurence of 1 after 0th position
print(numbers1.index(1, 1))
# index(search item,start position, stop position )
# print(numbers1.index(1, 14, 16))

# pass list to function


def negative_list(_list):
   negative = []
   for i in _list:
     negative.append(-i)
       
   return negative


print(negative_list(numbers))

