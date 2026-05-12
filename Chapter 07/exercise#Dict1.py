# exercise 
# define a function that takes a number (n)
# return a dictionary containing a cube of number from 1 to n 

# example
# cube_finder(3)
# {1:1,2:8,3:27}


def cube_finder(n):
  cubes_dic = {}
  for i in range(1, n + 1):
       cubes_dic[i] = i ** 3
  return cubes_dic


print(cube_finder(3))
