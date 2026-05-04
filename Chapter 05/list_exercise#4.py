# common element finder function
# define  a function which takes 2 list as input and return  a list
# Which contains common element of both list

# example

# input -->  [1,2,5,8],[1,2,7,6]
# output --> [1,2]


def common_finder(_list1, _list2):
  output_list = []
  for i in _list1:
    if i in _list2:
      output_list.append(i)
  return output_list


data_list1 = [1, 2, 5, 8]
data_list2 = [1, 2, 7, 6]

print(common_finder(data_list1, data_list2))
