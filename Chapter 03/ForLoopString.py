# For loop with string
name = "Harshit"
for i in range(0, len(name)):
    print(name[i])
    
print("\n Only allowed in Python since Strings are Iterable...")

name_python = "Nadeem"
for j in name_python:
      print(j)
      
# 1256 ----> 1 + 2 + 5 + 6
num_1 = input("Enter a number : ")
total = 0
for i in num_1:
  total += int(i)
print(f"Sum of digits of {num_1} = {total}")
