# args as Argument
# args here it is called as parameter
def multiply_fun(*args):
  mul = 1
  print(args)
  for i in args:
    mul *= i
  return mul


# this (1,2,4) here it is called as an argument
print(multiply_fun(1, 2, 4)) 

# let say here if we want to pass a list here
print("----Passing a list and unpacking and moving to tuple-----")
num_list = [1, 2, 3]
print(multiply_fun(*num_list)) 

# let say here if we want to pass a tuple here
print("----Passing a tuple and unpacking and moving to tuple-----")
num_tuple = (1, 2, 3)
print(multiply_fun(*num_tuple)) 
print(multiply_fun(num_tuple)) 
