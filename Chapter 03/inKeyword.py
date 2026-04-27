# in - Keyword is used to check if a value is present in a sequence (list, tuple, string) or not. It returns True if the value is found in the sequence, otherwise it returns False.
# The syntax of in keyword is as follows:
# value in sequence
# value not in sequence
# Example 1: Check if a value is present in a list
fruits = ['apple', 'banana', 'cherry'];
print('apple' in fruits); # True
print('grape' in fruits); # False
# Example 2: Check if a value is present in a string
name = "John Doe";  
print('John' in name); # True
print('Doe' in name); # True

# in keyword with if statement
# Check if the name contains the letter 'a'
name="Harshit";
if 'z' in name :
  print("Inside if statement");
  print("The name contains the letter 'a'.");
  print("End of if statement.");  
else:
  print("Inside else statement");
  print("The name does not contain the letter 'a'.");
  print("End of else statement.");  