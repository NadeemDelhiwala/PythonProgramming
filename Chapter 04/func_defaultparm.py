# Default parameters
def user_info(first_name, last_name, age=21):
  print(f"Your First Name : {first_name}")
  print(f"Your Last Name :  {last_name}")
  print(f"Your Age :        {age}")


print("Enter Details :")

first_name = input("Enter your First Name : ")
last_name = input("Enter your Last Name : ")
# age = int(input("Enter your Age : "))

print("========================")
print("User Information  ")
# user_info(first_name, last_name, age)
user_info(first_name, last_name)

print("========================")


def user_info_N(first_name, last_name='unknown', age=None):
  print(f"Your First Name : {first_name}")
  print(f"Your Last Name :  {last_name}")
  print(f"Your Age :        {age}")


print("========================")
print("User Information  ")
# user_info(first_name, last_name, age)
first_namep = input("Enter your First Name only..")
user_info_N(first_name)

print("========================")

# Default parameters should always be last parameter
# invalid
# def user_info_N(first_name, last_name='unknown', age):
