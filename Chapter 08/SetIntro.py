# set data types:
# unordered collection of unique items.

s = {1, 2, 3, 2}
print(s) 
# print(s[1]) not allowed since  it is sets are unordered collection

list_A = [1, 2, 3, 4, 5, 5, 5, 5, 6, 7, 7, 8]
print(list_A)
# now we want to remove duplicate
# step 1 -> convert list to set to remove duplicates
# step 2 -> convert set to list again to get unique elements
s2 = list(set(list_A))
print(s2)
print(type(s2))

# methods of sets

s_A = {1, 2, 3}
print('Adding elem to Set')
s_A.add(4)
s_A.add(5)
s_A.add(4)
print(s_A)
print(type(s_A))

print('Removing from Set')
s_A.remove(4)
print(s_A)
# s_A.remove(4)  # gives an error since 4 is already removed from set
s_A.discard(4)  # This will not give an error since 4 is already removed from set
print(s_A)

s_A.clear()
print(s_A)

s_B = {1, 2, 3}
s_C = s_B.copy()
print(s_B)
print(s_C)
print(s_B is s_C)
print(s_B == s_C)

# note: Inside set you cannot store list or dictionary or tuple
# s_E = {1, 1.1, 1.3, 'string'}
s_E = {1, 1.0, 1.3, 'string'}
# s_E = {1, 1.0, 1.3, 'string', []}
# s_E = {1, 1.0, 1.3, 'string', {}}
print(s_E)

