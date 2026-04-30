# function practice


def last_char(name):
  return name[-1]  # return last char(backward)


print(last_char("harshit vashisth"))

# even or odd


def odd_even_check(num):
    if num % 2 == 0:
      print("even")
    else:
      print("odd")

      
print(odd_even_check(10))
print(odd_even_check(5))

# one approach
# def odd_even_check_ret(num):
#     if num % 2 == 0:
#       return "even"
#     else:
#       return "odd"


# two approach
def odd_even_check_ret(num):
    if num % 2 == 0:
      return "even"
    return "odd"


print("+++++++++++++++++++++++++++++")
    
print(odd_even_check(10))
# print(odd_even_check(5))
print("=================================")
print(odd_even_check_ret(18))
print(odd_even_check_ret(17))

