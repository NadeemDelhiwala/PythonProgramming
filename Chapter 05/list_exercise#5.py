# last exercise
# function
# [1,2,3, [1,2],[3,4]] --> input
# output :2 (it will show many list exist inside our list)   
# Hint: use type()


def sublist_counter(_list):

   counter = 0
   for i in _list:
    if type(i) == list:
     counter += 1
   return counter   

 
mixed = [1, 2, 3, [1, 2], [3, 4], ["word1", "word2"]]
print(sublist_counter(mixed))
