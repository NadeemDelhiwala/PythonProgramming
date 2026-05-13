# def a function

name = ['harshit', 'mohit']

# print(func(names))

# print(func(names,reverse_str=True))


# using kwargs -> this argument may or may not exit
def func(nameslst, **kwargs):
  if kwargs.get('reverse_str') == True:
    return [name[::-1].title() for name in nameslst]
  else:
      return [name.title()  for name in nameslst]    

 
names = ['harshit', 'mohit'] 
print(func(names))
print(func(names, reverse_str=True))
