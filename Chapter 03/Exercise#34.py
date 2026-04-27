# problem
# ask user to input a number containing more than one digit 
# example: 1256
# calculate the sum of digits in that number using while loop

# algorithm
# 1. ask user to input a number
# 2. initialize a variable sum to 0 
# 3. use while loop to iterate through each digit in the number
# 4. in each iteration, extract the last digit of the number using modulus operator and add it to the sum variable
# 5. remove the last digit from the number using floor division operator         

num= input("Enter a number: ");
#1256
total=0;
i=0;
while i<len(num):
  total+=(int(num[i]));
  i=i+1;
print(f"Sum of digits in the number {num} is: {total}");   
