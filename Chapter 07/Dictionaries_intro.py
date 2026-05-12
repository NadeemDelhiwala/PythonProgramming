# dictionaries intro

# Q. Why we use dictionaries ?
# A => Because of limitation of list,lists are not enough to represent real data

# Example:
user = ['Harshit', 24, ['coco', 'kimi no na wa'], ['awakening', 'fairy tale']]
# this list contains username,age, fav music, fav tunes
# you can do this but this is not a good way

# Q - What are dictionaries
# A => Unordered collections of data in key : value pair.

# how to create dictionaries
user_dict1 = {'name': 'harshit', 'age':24}
print(user_dict1)
print(type(user_dict1))

# second way to create dictionary
user_dict2 = dict(name='Harshita', age=25)
print(user_dict2)
print(type(user_dict2))

# how to access data from dictionary we use key
# Note:- There is no indexing because of unordered collection of data
print(user_dict1['name'])
print(user_dict1['age'])

print(user_dict2['name'])
print(user_dict2['age'])

# Which type of data can dictionary store
# anything like numbers,string,list,dictionary

user_infodic = {
  'name':'Harsha',
  'age':52,
  'fav_movies':['coco', 'kimi no na wa'],
  'fav_tunes': ['awakening', 'fairy tale']
}
print(user_infodic)
print(user_infodic['name'])
print(user_infodic['age'])
print(user_infodic['fav_movies'])
print(user_infodic['fav_tunes'])

# storing dictionary inside a dictionary
dic_inside_dic = {
     "user1":  # This block of code is creating a dictionary with key-value pairs for user1's
     # information. The keys include 'name', 'age', 'fav_movies', and 'fav_tunes', each
     # storing specific information about user1. This dictionary is then being stored as a
     # value for the key "user1" inside the `dic_inside_dic` dictionary.
     {
            'name':'Harsha1',
             'age':51,
             'fav_movies':['coco', 'kimi no na wa'],
            'fav_tunes': ['awakening', 'fairy tale']
     },
   "user2": {
            'name':'Harsha2',
             'age':50,
             'fav_movies':['coco', 'kimi no na wa'],
            'fav_tunes': ['awakening', 'fairy tale']
     }
}

print(dic_inside_dic)

# how to add data to empty dictionary
user_info_empty = {}
user_info_empty['uname'] = 'Mohit'
user_info_empty['age'] = 23
print(user_info_empty)
print(user_info_empty['uname'])
print(user_info_empty['age'])
