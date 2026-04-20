# Exercise WATCH COCO
# Ask user's name and age
# If the user's name starts with 'a' or 'A'  and age is above 10, print "You can watch Coco". Otherwise, print "Sorry, you cannot watch Coco".

name=input("Enter your name: ");
age=int(input("Enter your age: ")); 
# approach #1
# if(name[0]=='a' or name[0]=='A') and age>10:
#     print("You can watch Coco");
# else:
#     print("Sorry, you cannot watch Coco");

# approach #2 
# We can also use the startswith() method to check if the name starts with 'a' or 'A'. The startswith() method returns True if the string starts with the specified prefix, otherwise it returns False.
if(name.startswith('a') or name.startswith('A')) and age>10:
    print("You can watch Coco");
else:
    print("Sorry, you cannot watch Coco");