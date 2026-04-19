number1=2;
print(number1);
number1=3;
print(number1);
#string,number,boolean
name="John";
print(name);
is_student=True;
print(is_student);
name="Alice";
print(name);  
is_student=False
print(is_student);
print("the data type of isStudent is",type(is_student ));
print("the data type of name is",type(name ));
print("the data type of number1 is",type(number1 ));
number1='two';
print(number1);
print("the data type of number1 is",type(number1 ));

#rules for naming variables
#1. variable names must start with a letter or an underscore
#2. variable names can only contain letters, numbers, and underscores 
#3. variable names cannot be a reserved keyword in Python
#4. variable names are case-sensitive
#5. variable names should be descriptive and meaningful
#examples of valid variable names
first_name="John";  
_last_name="Doe";
_age_2025=30;
#examples of invalid variable names
#1. 1st_name="John"; # starts with a number 
#2. first-name="John"; # contains a hyphen
#3. class="MyClass"; # reserved keyword 

#naming conventions for variables
#1. snake_case: words are separated by underscores (e.g., first_name, last_name)
#2. camelCase: the first word is lowercase and subsequent words are capitalized (e.g., firstName, lastName)
#3. PascalCase: each word is capitalized (e.g., FirstName, LastName)
#4. kebab-case: words are separated by hyphens (e.g., first-name, last-name) - not commonly used in Python
#best practice is to use snake_case for variable names in Python
first_name="John"; # snake_case
last_name="Doe"; # snake_case
middle_name="Smith"; # snake_case
full_name=first_name+" "+middle_name+" "+last_name;
print(full_name);

first_Hero="Superman"; # camelCase
Second_Hero="Batman";# PascalCase
print(first_Hero);
print(Second_Hero);

# first-name="John"; # invalid variable name, contains a hyphen
#print(first-name); # this will cause a syntax error

