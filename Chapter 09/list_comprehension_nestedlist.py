# list comprehension in nested list

example = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
nested_comp = [[i for i in range(1, 4)] for x in range(1, 4)]
print(nested_comp)

new_lst = []
for k in range(1, 4):
   new_lst.append([1, 2, 3])
   
print(new_lst)
