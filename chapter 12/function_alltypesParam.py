# functions with all parameters
# very important to understand

# PADK

# order in which it should be used in function
# Parameters
# Args
# Default parameters
# kwargs

# Parameters
# def func(a):


# Default parameters
def func(name='unknown', age=24):
    print(f"{name=}, {age=}")

    
# func(24)
# func()
# func('Nadeem')
func('Nadeem', 25)


def func_n(name, *args, last='unknown', **kwarg):
    print(f"{name=},{args=},{last=},{kwarg=}") 


func_n('harshit', 1, 2, 3, a=1, b=2)

# def funcpd(name,lastname="unknown"):
  
