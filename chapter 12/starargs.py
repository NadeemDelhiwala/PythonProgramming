# introduction to * args
# note Regex in python is pending to cover
# make flexible functions

# *operator
# *args


def total(a, b):
  return a + b


print(total(3, 4))
# TypeError: total() takes 2 positional arguments but 3 were given
# print(total(3, 4,5))


# to resolve this issue *args come in 
# (* args) this word "args" can be anything, but for convention purpose we use args
def all_total(*args):
  print(args)
  print(type(args))

  
all_total(1, 2, 3, 4, 5, 65)
# this function will take all arguments and create a tuple and then assign this function 
# this function will tuple as an argument
# t=(1,2,3,4,5,65)


def all_tot(* args):
   tot = 0
   for arg in args:
       tot += arg
   return tot     


all_tot(1, 2, 3, 4, 5, 65)
