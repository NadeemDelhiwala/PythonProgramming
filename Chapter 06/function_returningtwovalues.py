# function returning two values


def func(int1, int2):
  addition = int1 + int2
  multiplication = int1 * int2
  return addition, multiplication


print(func(2, 3))  # returns tuple

add, multi = func(2, 3)
print(add)
print(multi)
