# more about get , two same keys in dictionaries
users = {
 'name':'Harshit',
  'age': 24,
  'age':34
}
print(f"{users} and type is {type(users)}")
# returns value based on the key
print(users.get('name'))
print(users.get('names'))  # it will return None since names key is not available.
print(users.get('names', "No key exist with given key"))

