# define a function that take list of words as argument and 
# return list with reverse of every element in the last 

# example
# ['abc','tuv','xyz'] ---> ['cba',vut,zyx]


def reverse_element_list(_list): 
  elem_list = []
  for i in _list:
        elem_list.append(i[::-1])
  return elem_list


words = ['abc', 'tuv', 'xyz']
print(reverse_element_list(words))
