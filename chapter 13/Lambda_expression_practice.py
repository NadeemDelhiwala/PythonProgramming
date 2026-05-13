# lambda expression practice
def isEven(a):
   if a % 2 == 0:
     return True
   else:
     return False


print(isEven(3))
print(isEven(4))

print("Short way - I")


def isEven_s(a):
   if a % 2 == 0:
     return True
   return False


print(isEven_s(3))
print(isEven_s(4))

print("Short way - II")


def isEven_sa(a):
   return a % 2 == 0


print(isEven_sa(3))
print(isEven_sa(4))

print("\n---Lambda Expression:----")
isEven_lambda = lambda a:a % 2 == 0
print(isEven_lambda(3))
print(isEven_lambda(6))

isOdd_lambda = lambda a:a % 2 != 0
print(isOdd_lambda(3))
print(isOdd_lambda(6))


def last_char(s):
   return s[-1]

 
last_c = lambda s:s[-1]
print(last_c('Nadeem'))


# lamba expression with if else
def func(s):
    if len(s) > 5:
       return True
    return False 


func_lambda_ifelse = lambda s:True if len(s) > 5 else False
print(func_lambda_ifelse('abc'))
print(func_lambda_ifelse('abccdef'))

print('Without if else')


def funcls(s):
    return len(s) > 5 

  
func_lambda_ifelses = lambda s:len(s) > 5

print(func_lambda_ifelses('abc'))
print(func_lambda_ifelse('abccdef'))

