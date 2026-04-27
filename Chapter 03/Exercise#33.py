# sum of n natural numbers using while loop
# ask user for a number and calculate the sum of natural numbers from 1 to that number using while loop
# print total from 1 to n

total=0;
num=int(input("Enter a number: "));
i=1;
while i<=num:
   total+=i;
   i=i+1;
print(f"Sum of natural numbers from 1 to {num} is: {total}");
print("End of while loop");