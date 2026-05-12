# in keyword in  set and for loop

s = {'a', 'b', 'c'}

# in keyword to check if the item is present in set or not

if 'a' in s:
   print('Available in set')
else:
   print('Not available in set')

# for loop

for set_item in s:
     print(set_item)

list_Dup = [1, 2, 3, 3]
list_Uniq = list(set(list_Dup))
print(f"{list_Dup} and type is {type(list_Dup)}")
print(f"{list_Uniq} and type is {type(list_Uniq)}")

# set maths

sA_1 = {1, 2, 3, 4}
sA_2 = {3, 4, 5, 6}

# union
union_set = sA_1 | sA_2
print(sA_1)
print(sA_2)
print(union_set)

# intersection

intersection_set = sA_1 & sA_2
print(intersection_set)
