# add and delete data from dictionaries

user_info = {
  'name':'harshit',
  'age':24,
  'fav_movies': ['coco', 'kimi no na wala'],
  'fav_tunes':['awakening', 'fairy tale']
}
print(user_info)
# how to add data

user_info['fav_song'] = ['song1', 'song2']
print('After adding key-value pair')
print(user_info)

# pop method

print('....After removing elements....')
popped_items = user_info.pop('fav_tunes')
print(f"Popped item is {popped_items} and type is {type(popped_items)}")
print(user_info)
# note: pop(always have argument and cannot be blank)

# popitem method

print('----popitem method-----')
# used when you randomly want to delete a key-value pair
popped_items_randomly = user_info.popitem()
print(f"the randomly popped item is :{popped_items_randomly} and type is {type(popped_items_randomly)}")
print(user_info)
