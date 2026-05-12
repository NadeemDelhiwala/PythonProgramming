# in keyword and iteration in dictionary

print("----User Dictionary----")
user_info = {
  'name': 'Timmy',
  'age':25,
  'fav_movies':['coco', 'kimi no na wa'],
  'fav_tunes':['awakening', 'fairy tale']
}
print(user_info)
print("------------------------")
# check if key exist in dictionary
print('---check if key exist in dictionary---')
if 'name' in user_info:
    print('Congratulation the Key is available')
else:
    print('Unfortunately the Key is unavailable')

# check if value exist in dictionary
print('----check if value exist in dictionary----')
if 'Timmy' in user_info.values():
    print('Congratulation the value is available')
else:
    print('Unfortunately the value is unavailable')

print("---checking for complete list available or not")
print('----check if value exist in dictionary----')
if ['coco', 'kimi no na wa'] in user_info.values():
    print('Congratulation the value is available')
else:
    print('Unfortunately the value is unavailable')   

# Loops in dictionaries
print("---Loops in dictionaries to fetch all the keys---")
for i in user_info:
   print(i)  # will print all the keys

# Loops in dictionaries
print("---Loops in dictionaries to fetch all the values---")
for i in user_info.values():
   print(i)  # will print all the values

# values method

user_info_values = user_info.values()
print(user_info_values)
print(type(user_info_values))

user_info_keys = user_info.keys()
print(user_info_keys)
print(type(user_info_keys))

print("---Fetching values---")

for i in user_info:
    # print(i)
    print(f"{i} : {user_info[i]}")

# items method for running loops in dictionary
print("---Using items---")

user_items = user_info.items()
print(user_items)
print(type(user_items))
# [[('name', 'Timmy'), ('age', 25), ('fav_movies', ['coco', 'kimi no na wa']), ('fav_tunes', ###['awakening', 'fairy tale'])]]
# [(tuple 1),(tuple 2),(tuple 3)]

# key this can be any variable
# value this can be any variable
for key, value in user_info.items():
    print(f"Key:{key} and value :{value}")
