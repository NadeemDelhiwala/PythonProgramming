# some more methods to add data in our first
# insert method
# how to join(concatenate) two list
# extend method
# difference between append and extend method

fruits1 = ["mango", "orange"]
print(fruits1)
# insert method is used to insert element at a certain position
fruits1.insert(1, "grapes");  # grapes added to location 1
print(fruits1);
fruits1.insert(20, "woodapple");  # grapes added to last  location since index 20 is not available
print(".........Fruits 1 List.............")

print(fruits1)

# joining two list

fruits2 = ['banana', 'watermelon']
print(".........Fruits 2 List.............")
print(fruits2)

print("......Joined (Concatenated) list......")
fruits_joined = fruits1 + fruits2
print(fruits_joined)

# extend method
# case : if we need to add items of the list of fruit2 to fruit1 
print("...............Extend Method............")
fruits1.extend(fruits2)
print(fruits1);

# append method..
fruits3 = ['blueberry', 'cherry']
fruits1.append(fruits3)
print(fruits3);
print("...............append Method (list inside a list)............")

print(fruits1);

