#two inputs or multiple inputs
number1=input("Enter a number: ");
number2=input("Enter another number: ")
# name,age=input("Enter your name and age separated by a comma: ").split(","); # this will split the input string into a list of two elements, name and age
name,age=input("Enter your name and age separated by spaces: ").split(" "); # this will split the input string into a list of two elements, name and age
print("Entered Name:",name);
print("Entered Age:",age);

