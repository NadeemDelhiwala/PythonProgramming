# define  a function that take list of strings
# list containing reverse of every string
from test.libregrtest.utils import format_duration

# for example:
# l = ['abc','tuv','xyz']
# reverse_string(list)---> ['bac','vut','zyx']


def reverse_strings(list_strings):
    return [name[::-1] for name in list_strings]

  
lst_name = ['abc', 'tuv', 'xyz']
print(reverse_strings(lst_name))


def reverse_strings_n(list_str):
  new_list = []
  for name in list_str:
      new_list.append(name[::-1])
  return new_list  
 
  lst_name_n = ['abc', 'tuv', 'xyz']


print(reverse_strings_n(lst_name))     
