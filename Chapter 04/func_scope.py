# function scope

x = 5  # global variable


def func():
  x = 7
  return x


# print(x)  # not allowed since x is a local variable
def func2():
  # print(x)  # not allowed since x is a local variable
  print("tested")
  
  
print(func())  # return 7 since it local variable defined in the function
print(x);  # return 5 since it is a global variable


