# list comprehension with if statement
numbers = list(range(1, 11))
print(numbers)

# [1,2,3,4,5,6,7,8,9,10]
# even [2,4,6,8,10]

num_even_lst = []
for i in range(1, 11):
    if i % 2 == 0:
      num_even_lst.append(i)

print(num_even_lst) 

# now we will list comprehension with if statement
num_even_lst_lif = [i for i in numbers if i % 2 == 0]
print(num_even_lst_lif)

num_odd_lst_if = [i for i in numbers if i % 2 != 0]
print(num_odd_lst_if)

num_odd_lst_ifr = [i for i in range(1, 11) if i % 2 != 0]
print(num_odd_lst_ifr)
