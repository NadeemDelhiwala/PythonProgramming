# is vs == comparsion
# list compare
fruits1 = [
    "Apple",
    "Banana",
    "Orange",
    "Mango",
    "Grapes",
    "Pineapple"
    
]
fruits2 = [
    "Watermelon",
    "Apple"
    "Papaya",
    "Kiwi",
    "Peach",
    "apple",
    "Apple",
    "Cherry",
    "Guava",
    "Pear",
    "Blueberry",
    "Apple"
]
fruits3 = [
    "Apple",
    "Banana",
    "Orange",
    "Mango",
    "Grapes",
    "Pineapple",
]
 
print("...Our Fruits List 1...")

print(fruits1)

print("...Our Fruits List 2...")

print(fruits2)

print("...Our Fruits List 3...")

print(fruits3)

print(fruits1 == fruits2)
print(fruits1 == fruits3)  # values are same
print(fruits1 is fruits3)  # false since both are available in different location in the memory and both are different object
