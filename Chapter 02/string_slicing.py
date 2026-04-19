#string slicing
name="Python Programming";
print(name[0]); # this will print the first character of the string, which is "P"

#extracting more than one character
#syntax for slicing is string[start:end-1]

print(name[0:6]); # this will print the characters from index 0 to index  5, which is "Python"
print(name[7:11]); # this will print the characters from index 7 to index 9, which is "Pro"
print(name[0:]); # this will print the entire string, which is "Python Programming"
print(name[:6]); # this will print the characters from index 0 to index 5, which is "Python"
print(name[7:]); # this will print the characters from index 7 to the end of the string, which is "Programming"
print(name[:]); # this will print the entire string, which is "Python Programming"
print(name[13:18]); # this will print every second character of the string, which is "Pto rgamn"
print(name[-3:6]); # this will print the characters from index -3 to index 5, which is "Pro"