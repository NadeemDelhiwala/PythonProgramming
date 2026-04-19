#string formatting
name="John";
age=30;
#ugly way to format a string
print("Hello "+name+", you are "+str(age)+" years old."); # this will concatenate the string "Hello ", the value of name, the string ", you are ", the string representation of age, and the string " years old."
#smart way to format a string using f-strings
print(f"Hello {name}, you are {age} years old."); # this will replace the placeholders {name} and {age} with the values of the variables name and age respectively
#another way to format a string using the format() method
print("Hello {}, you are {} years old.".format(name,age)); # this will replace the placeholders {} with the values of the variables name and age respectively in the order they are passed to the format() method available in Python 3.6 and above
#another way to format a string using the % operator
print("Hello %s, you are %d years old." % (name, age)); # this will replace the placeholders %s and %d with the values of the variables name and age respectively available in Python 2 and above but not recommended in Python 3.6 and above because it is less readable and less efficient than f-strings and the format() method   

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++");
print("The name of a person is %s and the age is %d years old."%(name,age));
print(f"The name of a person is {name} and the age is {age} years old.");
print("The name of a person is {} and the age is {} years old.".format(name,age));
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++");

print("++++++++++++++++++++++++++++With some calculations+++++++++++++++++++++++++++++++++++++");
print("The name of a person is %s and the age is %d years old."%(name,age*2));
print(f"The name of a person is {name} and the age is {age*2} years old.");
print("The name of a person is {} and the age is {} years old.".format(name,age*2));
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++");