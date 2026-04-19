#user input
#input function is used to take input from the user
#inputfunction always returns a string
name=input("Enter your name: ");
print("Hello,"+name+"! Welcome to Python programming.");
print("The data type of name is",type(name));
age=input("Enter your age: ");
print("You are "+age+" years old.");
print("The data type of age is",type(age));
number1=input("Enter a number: ");
number2=input("Enter another number: ");
numberresult=number1+number2;
print("The result of adding the two numbers is: "+numberresult);
numberresult =int(number1)+int(number2);
print("The result of adding the two numbers is: "+str(numberresult));


#another way to convert the input to an integer
number3=int(input("Enter a number: "));
number4=int(input("Enter another number: "));
numberresult2=number3 + number4;
print("The result of adding the two numbers :: ",numberresult2);
print("The data type of numberresult2 is",type(numberresult2));
print("The result of adding the two numbers is: ",str(numberresult2));
print("The data type of adding the two numbers is: ",type(str(numberresult2)));

#float
num_f1=float(10);
print("The floating number : ",num_f1);
print("The data type of floating number : ",type(num_f1));