# Chapter 02 Summary

#strings
name="rharshitr";


#string indexing
print(name[1])
print(name[-1]);

#string slicing
print(name[0:3]);
print(name[0:5]);
print(name[0:-3]);  
print(name[0:-2]);
print(name[0:]);
print(name[3:]);
print(name[-4:]);
print(name[:-2:]);
print(name[0:5:1]);
print(name[0:5:2]);
name_s="Nadeem";
print(name_s[-1:0:-1]);
print(name_s[-2:0:-1]);
print(name_s[-2:0:1]);
# Key takeaway
# Negative indices let you count from the end of the string.

# The stop index is exclusive, so slicing ends just before it.

# A negative step reverses the direction of traversal

# Slice parameters for print(name_s[-2:0:1])
# 0  1  2  3  4  5
# N  a  d  e  e  m
# start = -2 → second-to-last character ('e' at index 4).

# stop = 0 → index 0 ('N'), but exclusive (so 'N' is not included).

# step = 1 → move forward (left to right).

# Direction conflict

# You’re starting at index 4 ('e') but moving forward with step=1.

# The stop=0 means “go until before index 0.”

# Since index 4 is already past index 0 in the forward direction, Python cannot collect any characters.

# Result  
# The slice is empty:

print(name_s[-2:-1:1])
print(name_s[-2:-1:-1])
print(name_s[-3:-2:-1])
print(name_s[-3:-5:-1])




#string input
age=int(input("enter your age:"));
print(age);

name_d,age_d=input("Enter your name and age : ").split();
print(name_d);
print(age_d);
# take two user inputs
name_d1,age_d1=input("Enter your name and age : ").split(",");
print(name_d1);
print(age_d1);
#len function
print(len(name_s));
#lower,upper, title method
print(name_s.upper());
print(name_s.lower());
print(name_s.title());

#find,replace,center method
print(name.find("r"));
print(name.find("r",1));

print(name.center(len(name)+8,"*"));
# string are immutable
print(name[1]);
print(name.replace("h","H",name.find("h")));
print(name);
