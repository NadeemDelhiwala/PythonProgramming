# define a function which will take a list containing numbers a input
# return list containing square of every elements

# exmaple :
# numbers = [1,2,3,4]
# square_list(number) ----> returns ------------> [1,4,9,16]

# approach 1

print("Approach 1")


def square_list(numbers_list):
   sqaures_list = []
   for number_list in numbers_list:
      sqaures_list.append(number_list * number_list)
   return sqaures_list


_list = [1, 2, 3, 4]
print(square_list(_list))

# approach 2

print("Approach #2")


def square_list_P(numbers_listP):
   sqaure_listP = []
   for number_listP in numbers_listP:
      sqaure_listP.append(number_listP ** 2)
   return sqaure_listP

 
_listP = [1, 2, 3, 4]
print(square_list_P(_listP))
