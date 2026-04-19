#String 
#collection of characters inside single or double quotes
#immutable - cannot be changed after creation
first_name="Harshit";
last_name="Vashisth";
full_name=first_name+" "+last_name;
print(full_name);
#string concatenation
# print(first_name+3); # this will cause a TypeError because we cannot concatenate a string and an integer
print(first_name+" "+ '3'); # this will work because we are converting the integer to a string before concatenation
print(first_name+" "+ "3"); # this will work because we are converting the integer to a string before concatenation
print(first_name+" "+ str(3)); # this will work because we are converting the integer to a string before concatenation 
print(first_name*3); # this will print the string three times
