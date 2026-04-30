def greater(a, b):
   if a > b:
     return a
   else:
    return b

# function inside function
# def new_greatest(a, b, c):
#       bigger = greater(a, b)
#       return greater(bigger, c)


def new_greatest(a, b, c):
      return greater(greater(a, b), c)


print(new_greatest(1200, 200, 3000))
