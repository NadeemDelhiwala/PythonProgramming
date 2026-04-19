#string methods part 1
name="HaRsHiT VaSHISThA";
print(name); # this will print the original string
# 1. lower() method - converts all characters in a string to lowercase
lower_name=name.lower(); # this will store the lowercase version of the string in the variable 
print(lower_name)
# 2.upper() method - converts all characters in a string to uppercase
upper_name=name.upper(); # this will store the uppercase version of the string in the variable
print(upper_name);

# 3. title() method - converts the first character of each word to uppercase and the rest to lowercase
title_name=name.title(); # this will store the title case version of the string in the variable
print(title_name);

# 4. swapcase() method - converts uppercase characters to lowercase and lowercase characters to uppercase
swapcase_name=name.swapcase(); # this will store the swap case version of the string in the variable
print(swapcase_name);

# 5. capitalize() method - converts the first character of a string to uppercase and the rest to lowercase
capitalize_name=name.capitalize(); # this will store the capitalized version of the string in the variable
print(capitalize_name);
#6. casefold() method - converts all characters in a string to lowercase and is more aggressive than lower() method
casefold_name=name.casefold(); # this will store the casefold version of the string in the variable
print(casefold_name);

#7. islower() method - returns True if all characters in a string are lowercase, otherwise returns False

result=name.islower(); # this will store the result of the islower() method in the variable
print(result); # this will print the result, which is False because the original string contains uppercase

#8. isupper() method - returns True if all characters in a string are uppercase, otherwise returns False
result=name.isupper(); # this will store the result of the isupper() method in the variable
print(result); # this will print the result, which is False because the original string contains lowercase

#9. istitle() method - returns True if the first character of each word in a string is uppercase and the rest are lowercase, otherwise returns False
result=name.istitle(); # this will store the result of the istitle() method in the variable
print(result); # this will print the result, which is False because the original string does not 
#10. isspace() method - returns True if all characters in a string are whitespace, otherwise returns False

#11. isalpha() method - returns True if all characters in a string are alphabetic, otherwise returns False
result=name.isalpha(); # this will store the result of the isalpha() method in the variable
print(result); # this will print the result, which is False because the original string contains whitespace

#12. isdigit() method - returns True if all characters in a string are digits, otherwise returns False
result=name.isdigit(); # this will store the result of the isdigit() method in the variable
print(result); # this will print the result, which is False because the original string contains alphabetic characters and whitespace

#13. isalnum() method - returns True if all characters in a string are alphanumeric (letters and numbers), otherwise returns False
result=name.isalnum(); # this will store the result of the isalnum() method in the variable
print(result); # this will print the result, which is False because the original string contains whitespace



#22. count() method - returns the number of occurrences of a substring in a string

result_count=name.count("H"); # this will store the result of the count() method in the variable
print(result_count); # this will print the result, which is 2 because the substring "h" occurs twice in the original string


#23. find() method - returns the index of the first occurrence of a substring in a string, or -1 if the substring is not found

print("############find method###########");
string_find="she is beautiful and she is good dancer";
# string_find="is she is beautiful and she is good dancer";

stringfind_pos=string_find.find("is");
print(string_find);

print(f"The position of word is :{stringfind_pos}")

# to find from specific position
stringfind_pos_given=string_find.find("is",1);
print(f"The specific position of word is :{stringfind_pos_given}")



#dynamically finding the position
ispos_1=string_find.find("is"); # 4th pos of is is returned
ispos_2=string_find.find("is",ispos_1 + 1);
print(f"Dynamic position is {ispos_2}")

print(f"Dynamic position is  {string_find.find("is",string_find.find("is")+1)}")

# 23.1 center
string_center="Nadeem";
center_res=string_center.center(len(string_center)+4,"*");
center_res_onestar_right=string_center.center(len(string_center)+1,"*");

print(center_res);
print(center_res_onestar_right);


# Program to print 4 **** to the left and right of the name (Name should be taken dynamically)
cen_name=input("Enter the name : ");
print(cen_name.center(len(cen_name)+8,"*"))








#24. rfind() method - returns the index of the last occurrence of a substring in a string, or -1 if the substring is not found

#25. index() method - returns the index of the first occurrence of a substring in a string, or raises a ValueError if the substring is not found

#26. rindex() method - returns the index of the last occurrence of a substring in a string, or raises a ValueError if the substring is not found

#27. startswith() method - returns True if a string starts with a specified substring, otherwise returns False
result_startswith=name.startswith("Ha"); # this will store the result of the startswith() method in the variable
print(result_startswith); # this will print the result, which is True because the original
#28. endswith() method - returns True if a string ends with a specified substring, otherwise returns False

#29. strip() method - removes leading and trailing whitespace from a string
spaces_name="   HaRsHiT    ";
dots="...................";

#30. lstrip() method - removes leading whitespace from a string from left side of the string
lstrip_name=spaces_name.lstrip(); # this will store the left stripped version of the string in the variable
print(spaces_name + dots);
print(lstrip_name + dots) # this will print the left stripped version of the string, which is

#31. rstrip() method - removes trailing whitespace from a string 
rstrip_name=spaces_name.rstrip(); # this will store the right stripped version of the string in the variable
print(rstrip_name + dots); 

stripped_name=spaces_name.strip(); # this will store the stripped version of the string in the variable
print(stripped_name + dots); # this will print the stripped version of the string, which is "HaRsHiT" without any leading or trailing whitespace
#32. replace() method - replaces all occurrences of a specified substring with another substring in a string
space_inbetween_name="Ha Rs Hi T";
replace_name=space_inbetween_name.replace(" ", ""); # this will store the version of the string with spaces removed in the variable
print(space_inbetween_name); # this will print the original string with spaces, which is "Ha Rs Hi T
print(replace_name); # this will print the version of the string with spaces removed, which

string_sen="she is beautiful and she is good dancer";
# replace spaces with underscores
replace_res=string_sen.replace(" ","_");
replace_word=string_sen.replace("is","was");
print(string_sen);
print(replace_res);
print(replace_word);
replace_first_occurence=string_sen.replace("is","was",1);
print(replace_first_occurence);

#33. split() method - splits a string into a list of substrings based on a specified delimiter
#34. join() method - joins a list of strings into a single string using a specified delimiter
#35. partition() method - splits a string into three parts based on a specified separator and returns a tuple containing the part before the separator, the separator itself, and the part after the separator
#36. rpartition() method - splits a string into three parts based on a specified separator and returns a tuple containing the part before the separator, the separator itself, and the part after the separator, starting from the right side of the string

#44. len() method - returns the length of a string
length=len(name); # this will store the length of the string in the variable length
print(length); # this will print the length of the string, which is 17
print(len(name)); # this will print the length of the string, which is 17
print(len("Harshit")); # this will print the length of the string, which is 7
#45. min() method - returns the smallest character in a string based on ASCII values  
result_min=min(name); # this will store the smallest character in the string based on ASCII values in the variable result_min
print(result_min); # this will print the smallest character in the string based on ASCII values,
#46. max() method - returns the largest character in a string based on ASCII values
result_max=max(name); # this will store the largest character in the string based on ASCII values in the variable result_max
print(result_max); # this will print the largest character in the string based on ASCII values,
#47. ord() method - returns the ASCII value of a character
result_ord=ord("H"); # this will store the ASCII value of the character "H" in the variable 
print(result_ord); # this will print the ASCII value of the character "H", which is 72
#48. chr() method - returns the character corresponding to an ASCII value
result_chr=chr(72); # this will store the character corresponding to the ASCII value 72 
print(result_chr); # this will print the character corresponding to the ASCII value 72, which is "H"

