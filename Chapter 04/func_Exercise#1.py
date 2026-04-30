# define a function which takes two numbers as input and returns greater of the two number
def greater_two(a, b):
   if a > b:
     return a
   else:
    return b


num1 = int(input("Enter num1 :"))
num2 = int(input("Enter num2 :"))

bigger = greater_two(num1, num2)
print(f"{bigger} is greatest")

# define a function which takes three numbers as input and returns greater of the three number
# def greater_three(a, b, c):
#    if a > b and a > c:
#      return a
#    elif b > a and b> c:
#       return b
#    else:
#        return c


def greater_three(a, b, c):
   if a > b and a > c:
     return a
   elif b > c:
      return b
   else:
       return c


print("=====================================")
print("Calculate greatest of three nums")
num1 = int(input("Enter num1 :"))
num2 = int(input("Enter num2 :"))
num3 = int(input("Enter num3 :"))

big_val = greater_three(num1, num2, num3)
print(f"{big_val} is greatest")

