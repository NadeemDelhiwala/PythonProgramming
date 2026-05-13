# * args with normal parameters
def multiply_nums(*args):
  multiplication = 1
  for arg in args:
     multiplication *= arg
  return multiplication


print("---Without argument")
print(multiply_nums())
print("---Without argument")
print(multiply_nums(1, 2, 3))
print(multiply_nums(1, 2, 3, 4))

  
def multiply_nums_n(nums, *args):
  multiplication = 1
  print(f"{nums=}")
  print(f"{args=}")
  
  for arg in args:
     multiplication *= arg
  return multiplication


   # num =2 and args will have tuple(2,36)
print(multiply_nums_n(2, 2, 36))

   # num =24 and args will have tuple(2,4)
print(multiply_nums_n(24, 2, 4))

# this will give an error since we have a normal defined as num
# print(multiply_nums_n())


def multiply_nums_na(num1, num2, *args):
  multiplication = 1
  print(f"{num1=}")
  print(f"{num2=}")
  print(f"{args=}")
  
  for arg in args:
     multiplication *= arg
  return multiplication


# here num1 =24, num2=2, args=()
print(multiply_nums_na(24, 2))

print("----------------")
# here num1 =24, num2=2, args=(3,4)

print(multiply_nums_na(24, 2, 3, 4))

# if we supply normal parameter after args then

print("-----if we supply normal parameter after args then----")


# this not allowed.
def multiply_nums_naf(*args, num1, num2,):
  multiplication = 1
  print(f"{num1=}")
  print(f"{num2=}")
  print(f"{args=}")
  
  for arg in args:
     multiplication *= arg
  return multiplication

# this is not allowed since we have passed *args as first parameters if we call the function then all argument will go in args and no argument will go in num1, num2
# print(multiply_nums_naf(24, 2, 3, 4))
