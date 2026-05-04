# List inside a list
# this is a 2d List
matrix_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 3 items in the list 
print(matrix_list[0])
print(matrix_list[1])
print(matrix_list[2])

print("+++++++++++++++++++++++++++++")
for sublist in matrix_list:
    for i in sublist:
        print(i)
    print("+ + + + + + +")

print("Accessing the value...")
print(matrix_list[1][1])

s = "string"
print(type(s))
print(type(matrix_list))
