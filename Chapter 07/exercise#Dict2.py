user = {
  'name':'harshit',
  'age':24,
  'fav_movies':['coco', 'avengers'],
  'fav_songs':['song1', 'song2']
}

print(user)

# user input and add it to the dictionary
user_info = {}
u_name = input("Enter your name : ")
u_age = input("Enter your age : ")
u_fav_movies = input("Enter your fav movies separated by comma : ").split(",")
u_fav_songs = input("Enter your fav song separated by comma : ").split(",")

user_info['u_name'] = u_name
user_info['u_age'] = u_age
user_info['u_fav_movies'] = u_fav_movies
user_info['u_fav_songs'] = u_fav_songs

print("---User information----")

print(user_info)

print('--Looping---...')

for key, value in user_info.items():
    print(f"{key}:{value}")
