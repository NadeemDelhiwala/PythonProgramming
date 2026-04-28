# practice for loop
# ask the user and count each character
# "Harshit Vashisth"
# H:1
# a:2
# r:1
# s:3
# h:3
# i:2
# t:2
#  :1
# V:1
  
name = input("Enter your name : ")
temp_var = "";
for i in range(0, len(name)):
   if name[i] not in temp_var:
     print(f"{name[i]} : {name.count(name[i])}")
     temp_var += name[i];
     
print("End of the program...")
