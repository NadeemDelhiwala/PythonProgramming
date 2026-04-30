# iseven_checker function
def iseven_check(num):
    if num % 2 == 0:
        return True
    else:
     return False

    
print(iseven_check(9))
print(iseven_check(4))


def iseven_check1(num):
    if num % 2 == 0:
        return True
    return False

    
print(iseven_check1(11))


def iseven_check2(num):
    if num % 2 == 0:
        return True
    else:
     return False

    
print(iseven_check2(9))
print(iseven_check2(4))


def isEven_small(num):  # parameters
    return num % 2 == 0


print(isEven_small(5))  # argument
print(isEven_small(4))


# function without params
def song():
 return "happy birthday song"


print(song())

