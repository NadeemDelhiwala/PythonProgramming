#Ask user to input 3 numbers and you have to print the average of three number using string formatting

# Bonus Tip:Try to take all the three comma separated inputs in one line.
num1,num2,num3=(input("Enter three numbers separated by commas: ").split(","));
average_result=int(num1)+int(num2)+int(num3);
average_result=average_result/3;
print("The average of three numbers is: "+str(average_result)+" .");
# another way to print the average of three numbers using f-strings
print(f"The average of three numbers is: {average_result} .");
print("The average of three numbers is: {} .".format(average_result));
print("The average of three numbers is: %f ." %(average_result));

print("++++++++++++++++++++++++++Individual Inputs+++++++++++++++++++++++++++++++++++++++");
#individual inputs
num4=int(input("Enter a number: "));
num5=int(input("Enter another number: "));
num6=int(input("Enter another number: "));
avg_res=num4+num5+num6/3;
print("The average of three numbers is: "+str(avg_res)+" .");
print("The average of three numbers is {}".format(avg_res));
print(f"The average of three number is {avg_res} .");
print("The average of three numbers is: %f ." %(avg_res));