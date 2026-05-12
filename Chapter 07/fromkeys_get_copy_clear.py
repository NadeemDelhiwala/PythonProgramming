# from keys method --> is used to create dictionary
# d={'name':'unknown','age':'unknown'}

d_list = dict.fromkeys(['name', 'age', 'height'], 'unknown')
d_tuple = dict.fromkeys(('name', 'age', 'height'), 'unknown')
d_string = dict.fromkeys("abc", "unknown")
d_range = dict.fromkeys(range(1, 6), "unknown")
d_listA = dict.fromkeys(['name', 'age'], ['unknown', 'unknown'])
print(f"{d_list} and type {type(d_list)}")
print(f"{d_tuple} and type {type(d_tuple)}")
print(f"{d_string} and type {type(d_string)}")
print(f"{d_range} and type {type(d_range)}")
print(f"{d_listA} and type {type(d_listA)}")

# get method (useful)
d_getA = {'name':'Harshita', 'age':'unknown'}
# to access key from this dictionary
print(d_getA['name'])
# print(d_getA['names']) # gives an error since the key does not exist to handle this situation we used get() method to access keys

print(d_getA.get('name')) 
print(d_getA.get('names'))  # this will not give an error instead it will return None

# You can also use to check the existence of key
# approach 1
if 'name' in d_getA:
     print('Key is available')
else:
  print('Key not available')
  
# approach 2
if d_getA.get('name'):
     print('Key is available - get() method')
else:
  print('Key not available -  get() method ')

# clear method
print('---Clear method---')
d_getA.clear()
print(d_getA)

d_getC = {
  'name':'Ronit',
  'age':24,
  'hobbies':['singing', 'playing', 'reading']
}

print('Creating exact copies of the dictionary')
d_getD = d_getC.copy()

print(d_getC)
print(d_getD)
print(d_getD.popitem())
print(d_getC) 
print(d_getD)  # copy
print(d_getC is d_getD)  # check if both are pointed to the same memory location
print(d_getC == d_getD)  # check if both are have data but does not same memory location
# if we write something like this.
print("-------------------------")
d_getD = d_getC  # they are not copies instead they are pointing to the same dictionary
print(d_getC is d_getD)  # check if both are pointed to the same memory location
print(d_getC == d_getD)  # check if both are have data but does not same memory location
print(d_getD.popitem())
print(d_getC)
print(d_getD)

