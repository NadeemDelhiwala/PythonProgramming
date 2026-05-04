# join and split
# split method

 # convert string \to list
user_1 = 'harshit 24'.split()
print(user_1)

user_2 = 'harshit,24'.split(',')
print(user_2)

username, age = 'harshit 24'.split()
print(f"username = {username}")
print(f"age = {age}")

username1, age1 = input("Enter your name and age separated by spaces ").split()
print(f"username1  = {username1}")
print(f"age1 = {age1}")

 # join method
  # convert list to string
print("Join method")
user3_info = ['harshit', '24']
print(','.join(user3_info))

# Note : Both the parameters should be in the string else it will give an error
