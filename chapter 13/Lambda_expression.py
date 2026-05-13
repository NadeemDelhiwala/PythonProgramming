# Lambda Expression (anonymous Function)


def add(a, b):
  return a + b


# assign lambda to a variable
add_variable = lambda a, b:a + b

print(add_variable(2, 4))

# we use lambda expression with built-in functions, like map, reduce, filter

mul = lambda a, b:a * b
print(mul(2, 4))


