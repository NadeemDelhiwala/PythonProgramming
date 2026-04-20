# and or conditional statements are used to combine multiple conditions in a single if statement. The syntax of an and or conditional statement is as follows:
# if condition1 and condition2:
#     # code to execute if both conditions are true
# if condition1 or condition2:
#     # code to execute if at least one condition is true
name='abc';
age=19;
if name=='abc' and age==19:
    print("Inside if statement");
    print("Name is abc and age is 19.");
    print("End of if statement.");
else :  
    print("Inside else statement");
    print("Name is not abc or age is not 19.");
    print("End of else statement.");  


roll_no=123;
subject='python';
if roll_no==124 or subject=='pythoni':
    print("Inside if statement");
    print("Roll number is 123 or subject is python.");
    print("End of if statement.");
else :  
    print("Inside else statement");
    print("Roll number is not 123 and subject is not python.");
    print("End of else statement.");  