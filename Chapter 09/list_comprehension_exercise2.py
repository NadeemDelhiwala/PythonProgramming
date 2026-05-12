def numToString(lst):
  return [str(i) for i in lst if (type(i) == int or type(i) == float)]


print(numToString([True, False, [1, 2, 3], 1, 1.0, 3]))
