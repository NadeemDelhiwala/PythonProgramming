# define a function which will take list as an argument and this function will return a 
# reversed # list

# example:
# [1,2,3,4]  -----> [4,3,2,1]
# ['word1','word2','word3'] --->  ['word3','word2','word1']

# Note : you can simply do this exercise by using reverse method or [::-1]


def reverse_list(_lst):
    _lst.reverse()
    return _lst

  
numbers = [1, 2, 3, 4]

print(reverse_list(numbers))


def reverse_list1(_lst1):
    return _lst1[::-1]


numbers1 = [1, 2, 3, 4]

print(reverse_list1(numbers1))

# but try to do this with the help of append and pop method


def reverse_list2(_lst2):
  pop_item = ""
  pop_item += _lst2.pop()
  return pop_item

# numbers2 = [1, 2, 3, 4]
# result = ""

# for i in range(len(numbers2)):
#     pop_item = numbers2.pop()
#     result += str(pop_item) + ", "

# # remove trailing comma and space
# result = result.rstrip(", ")
# print(result)
    
  # print(reverse_list2(numbers2))

  
def reverse_list5(lst):
     r_list = []
     for i in range(0, len(lst)):
        pop_item = lst.pop()
        r_list.append(pop_item)
     return r_list


numbers5 = [1, 2, 3, 4]
print(reverse_list5(numbers5))
