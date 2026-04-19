# *********************summary of chapter 1*********************
# print Function
print("Hello, World!");
print('hello,"World!" From Python');
print("hello,'World!' From Python");
print("hello,\"World!\" From Python");
print('hello,\'World!\' From Python');

#escape sequences
#escape sequences are special characters that are used to represent certain characters in a string. They are preceded by a backslash (\) and are used to represent characters that cannot be easily typed or that have special meaning in Python. Some common escape sequences include:
print("This is a new line.\nThis is the second line."); # \n is used to create a new line
print("This is a new line.\tThis is the second line."); # \n is used to create a new line

#escape sequence as normal text
print(r"This is a new line.\nThis is the second line."); # r is used to treat the string as raw text, so the escape sequences are not processed
# python as calculator
print(2+3); # addition
print(5-2); # subtraction
print(4*3); # multiplication
print(10/3); # division (float division)
print(10//3); # floor division (integer division)
print(10%3); # modulus
print(2**3); # exponentiation
print((2+3)*4); # parentheses to change the order of operations
print(2**4**2); # exponentiation
print(2**3**2); # exponentiation
print((2+3)*4/2);
#variables
#rules for naming variables
name="John";
print(name);
print("the data type of name is",type(name));
name=123;
print(name);
print("the data type of name is",type(name));

#conventions for naming variables
user_one="Alice"; # snake_case
userTwo="Bob"; # camelCase
UserThree="Charlie"; # PascalCase
print(user_one);
print(userTwo);
print(UserThree);
