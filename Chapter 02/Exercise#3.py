# take two comma separated values as input from user
# 1.username example: "john"
# 2.single character example: "a"

name,chars=input("Enter your name and a character separated by a comma: ").split(","); # this will split the input string into a list of two elements, name and chars
#output:  2 lines

#1. username length
#2.count of the character that user entered (bonus: case insensitive count of the character)
print(f"Length of the username is: {len(name)}");
print(f"Count of the character '{chars}' in the username is: {name.lower().count(chars.lower())}"); # this will count the number of occurrences of the character chars in the string name

#solving the same problem using strip method to remove any leading or trailing whitespace from the input string
print("Using strip method to remove any leading or trailing whitespace from the input string:");
print(f"Count of the character '{chars}' in the username is: {name.lower().strip().count(chars.lower().strip())}"); # this will count the number of occurrences of the character chars in the string name
