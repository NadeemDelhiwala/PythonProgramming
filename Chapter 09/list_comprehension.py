# list comprehension
# with the help of list comprehension, we can create of list in one line

# create a list of squares from 1 to 10

# Normal Approach of creating and using list
squares = []
for i in range(1, 11):
    squares.append(i ** 2)
print(squares)   

# list comprehension approach

squares_2 = [i ** 2 for i in range(1, 11)]
print(squares_2)

negative_num = []
for i in range(1, 11):
    negative_num.append(-i)
print(negative_num)

negative_num_2 = [-i for i in range(1, 11)]
print(negative_num_2)

names = ['Harshit', 'Mohit', 'Rohit']
new_list_names = []
for name in names:
    new_list_names.append(name[0])
print(new_list_names)

new_list_names_ls = [name[0] for name in names]
print(new_list_names_ls)
