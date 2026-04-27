# if..elif..else statement is used to execute a block of code based on a condition. It is a way to control the flow of the program. The syntax of an if..elif..else statement is as follows:
# if condition1: 
#     # block of code
# elif condition2:
#     # block of code
# else:
#     # block of code
# show ticket price based on age
# 0-3 years: (free) 
# 4-10 years: (150)
# 11-60 years: (250)
# above 60 years: (200)
# approach - 1

age=int(input("Enter your age: "));
if age<=0 :
  print("Inside if statement");
  print("Your ticket price is free since you are 0 years old.");
  print("End of if statement.");
elif age>=0 and age<=3 :
  print("Inside elif statement");
  print("Your ticket price is free since you are between 0 and 3 years old.");
  print("End of elif statement.");
elif age>=4 and age<=10:
  print("Inside elif statement");
  print("Your ticket price is 150.");
  print("End of elif statement.");
elif age>=11 and age<=60:
  print("Inside elif statement");
  print("Your ticket price is 250.");
  print("End of elif statement.");
else:
  print("Inside else statement");
  print("Your ticket price is 200.");
  print("End of else statement.");

# approach - 2

# age=int(input("Enter your age: "));
# if 0<=age<=3 :
#   print("Inside if statement");
#   print("Your ticket price is free.");
#   print("End of if statement.");
# elif 4<=age<=10:
#   print("Inside elif statement");
#   print("Your ticket price is 150.");
#   print("End of elif statement.");
# elif 11<=age<=60:
#   print("Inside elif statement");
#   print("Your ticket price is 250.");
#   print("End of elif statement.");
# else:
#   print("Inside else statement");
#   print("Your ticket price is 200.");
#   print("End of else statement.");