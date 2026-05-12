user_info = {
  'name':'harshit',
  'age':24,
  'fav_movies': ['coco', 'kimi no na wala'],
  'fav_tunes':['awakening', 'fairy tale']
}

print(user_info)
more_info = {
  'State':'Haryana',
  'hobbies':['coding', 'reading', 'guitar']
}
# now we want to add mpre_info data to our user_info dictionary

user_info.update(more_info)
print("---After updating the user dictionary---")

print(user_info)

# let say if you have same key in 2 dictionary
user_infoA = {
  'name':'harshit',
  'age':24,
  'fav_movies': ['coco', 'kimi no na wala'],
  'fav_tunes':['awakening', 'fairy tale']
}

print(user_info)
more_infoA = {
   'name': 'harshit Vashishth',
   'State':'Haryana',
  'hobbies':['coding', 'reading', 'guitar']
}

user_infoA.update(more_infoA);
print('-----\n-----')
print(user_infoA)

# if we pass any empty {} then nothing will get updated
print("---using update with {}----")
user_infoC = {
  'name':'Mohan',
  'age':55,
  'fav_movies': ['Toco', 'Yimi no na wala'],
  'fav_tunes':['Raining', 'Dairy tale']
}
user_infoC.update({})
print(user_infoC)
