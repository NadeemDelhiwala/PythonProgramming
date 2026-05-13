# define a function 
# input
# num , iterable(tuple, list) containing numbers as args

# example
# nums=[1,2,3]
# to_power(3,*nums)

# output
# list --> [1**3,8,27]

# if user did not pass any args then it should  give an message 'hey you did not pass  args
# else
# return list

# Note Use list comprehension
lst = []
if lst:
    print("Not empty")
else:
  print("Empty")
  
  # or both are same
lst1 = []
if len(lst1) > 0: 
    print("Not empty")
else:
  print("Empty")


def to_power(num, *args):
  if args:
     return [i ** num for i in args]
  else:
    return "You did'nt pass any args."

  
nums_lst = [1, 2, 3]
  
print(to_power(2, *nums_lst))
print(to_power(2))
print(to_power(2, *[3, 4]))
