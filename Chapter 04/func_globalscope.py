# function scope

x = 5


def func():
   global x 
   x = 7
   return x

# print(x)  # not allowed since x is a local variable


print(x);  # return 5 since it global variable defined in the function   
print(x);    
print(func())  # return 7 since it global variable accessed in the function
print(x);  # return 7 since it global variable defined in the function
