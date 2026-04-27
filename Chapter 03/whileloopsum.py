# Sum of natueral numbers using while loop 1 to 10
num=int(input("Enter a number: "));
sum=0;
i=1;
while i<=num:
    # sum=sum+i;  
    sum+=i;
    i=i+1;
print(f"Sum of natural numbers from 1 to {num} is: {sum}");