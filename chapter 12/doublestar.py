# kwargs (keyword arguments)
# ** kwargs (double star operator)

# kwaargs as a parameter


def func(**kwargs):
   print(kwargs)
   print(type(kwargs))
   for k, v in kwargs.items():
     print(f"{k} :{v}")


# *args -> it take as tuple and it can accept any number of argument
# **args or kwargs --> will take keyword as dictionary and print dictionary  
func(first_name='harshit', last_name='vashistha')


def func1(nme, **kwargs):
   print(kwargs)
   print(type(kwargs))
   for k, v in kwargs.items():
     print(f"{k} :{v}")


# *args -> it take as tuple and it can accept any number of argument
# **args or kwargs --> will keyword as dictionary and print dictionary  
func(first_name='harshit', last_name='vashistha')
print('--------')

func1("jasmin", first_name='harshit', last_name='vashistha')

print('Dictionary unpacking')
dict = {'name':'Harry', 'age':24}
func(**dict)
# func(dict)
