# Data structures
# list --> this chapter
# ordered collection of items

# you can store anything in list int, float, string

# creating the list for storing numbers
numbers = [1, 2, 3, 4]

# printing the list
print(numbers)

# creating the list for storing string
words = ["word1", "word2", "word3"]
# printing the list
print(words)

# creating the list for storing mixed elements
mixed = [1, 2, 3, "five", "six", 2.5, None]
# printing the list
print(mixed)

# accessing the list elements 
# [0 ,1, 2, 3] => position
# [1, 2, 3, 4] => list elements
print(numbers[3])

# [ 0 ,     1,           2]  => position
# ['word1', 'word2', 'word3'] = > list elements
print(words[2])
print(words[:2:])  # slicing used to extract a part of list

# [ 0 ,1, 2,  3,       4,   5,   6] =>position
# [1, 2, 3, 'five', 'six', 2.5, None] = > list elements
print(mixed[4])
print(mixed[-1])  # access and extract last position

# change the mixed elem

mixed[1] = "two"
print("...Modified mixed list....")
print(mixed)

# `mixed[1:] = "two"` is trying to assign the string "two" to a slice of the `mixed` list starting
# from index 1 onwards. However, this operation will not replace the elements in the list with the
# string "two" as intended. Instead, it will replace the elements in the slice with the single string
# "two".
# mixed[1:] = "two"
# print(mixed)

mixed [1:] = ["three", "four", "five"]
print(mixed)

