print('Hello World!!!')
print("Hello World!!!")
print("Hello 'world' World!!!")
print('Hello "world" World!!!')
# print('Hello 'world' World!!!')

print(" I 'm a Python programmer");

# escape character
print("We are \"super\"'s programmers");
print('We are \'super\'s programmers');
print("I\'m a Python programmer");

print("Line A");
print("Line B");
print("Line C\nLine D");
print("name:\tNadeem");
print("name:\ Nadeem");
print("name: Nadeem\\"); 
print("name: Nadeem\\\\"); 
print("hell\blo world");

# print("hell\blo world");

print("Line A \\n Line B");
print("Line A \\t Line B");
print("this is a dpuble backslash \\\\");
print("\\\" \\'");

# Exercise
print("#**************************print the following lines**************************");
print("this is \\\\ double backslash");
print("these are /\/\/\/\/\ mountain");
print("he is\tawesome");
print("\\\" \\n \\t \\'");

# Raw String
print(r"Line A \n Line B");
print(r"Line A \t Line B");
print(r"\" \n \t \'");

#emoji
print("😀");
print("\u2764");
print("\U0001F600");
print("\U0001F604");
print("\U0001F607");

# Operators
print(2 + 3);
print(2 - 3); 
print(2 * 3);
print(15 / 2); #floating point division
print(14 // 2); # floor division (integer division)
print(15 % 2);
print(2 ** 3);
print(2**0.5); # square root of 2
print(round(2**0.5, 4)); # round to 4 decimal places

# Precedence of operators and Associativity rules
print(2 + 3 * 4); # multiplication has higher precedence than addition  
print((2 + 3) * 4); # parentheses have the highest precedence
print(2 ** 3 ** 2); # exponentiation is right associative
print((2+3)*5/2%6)
#5 * 5 / 2 % 6
# Parentheses : Highest precedence
# Exponent : Right to Left
# Predence: *, /, % have the same precedence and are evaluated from left to right
# Predence: +, - have the same precedence and are evaluated from left to right

# 5 * 5 / 2 % 6 Executing from left to right  
# 25 / 2 % 6
# 12.5 % 6
# 0.5

# Exponentiation is right associative
print(2 ** 3 ** 2); # 2 ** (3 ** 2) = 2 ** 9 = 512