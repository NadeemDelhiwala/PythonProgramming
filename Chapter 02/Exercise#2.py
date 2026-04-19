#Ask userName and print back userName in reverse order
# Note: Try to make your program in 2 lines using string formatting.
name=input("Enter your name: ");
name_reverse=name[-1::-1]; 
print(f"Your name in reverse is: {name_reverse}"); #will reverse the string using slicing
print(f"Your name in reverse is: {name[::-1]}");

