# ask a user to input the name
# Example: Harshit Vashisth
# print count of each letter in the name using while loop

# input:
   # H :1
    # a :2  
    # r :1
    # s :3
    # h :3
    # i :2
    # t :2
    # space :1
    # V :1
    

# name=input("Enter your name: ")
# Harshit Vashisth
# temp_var = "" 
# i=0;
# while i < len(name):
#      if name[i] not in temp_var: # check if the letter is already counted or not
#         temp_var +=name[i]; # add the letter to the temp_var to keep track of the counted letters
#         print(f"{name[i]} : {name.count(name[i])}");
#      i=i+1;
# print("End of while loop");


name=input("Enter your name: ");
temp_var=""
i=0;
while i < len(name):
     if name[i] not in temp_var:
        temp_var+=name[i];
        print(f"{name[i]}:{name.count(name[i])}"); 
     i=i+1;
print("End of while loop");
    
   