# dictionary comprehension
# square ={key:value,Key:value}
# square={1:1,2:4,3:9}

square_dict = {num:num ** 2 for num in range(1, 11)}
print(square_dict)

square_dict_f = {f"Square of {num} is ":num ** 2 for num in range(1, 11)}
print(square_dict_f)

print("Printing in different line we use for loop")
for k, v in square_dict_f.items():
  print(f"{k}:{v}")

stringchar = "harshit"

word_count = {char:stringchar.count(char) for char in stringchar}
print(word_count)
