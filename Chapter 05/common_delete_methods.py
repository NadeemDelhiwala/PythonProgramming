# common methods to delete data from list
fruits = ['orange', 'Woodapple', 'apple', 'pear', 'banana', 'kiwi', 'Pineapple', 'Woodapple', 'Custardapple']
# pop  method to delete data (deletes last element by default if no args are passed)
print("............Before Deleting elements............")
print(fruits)
fruits.pop()
print("............After Deleting elements............")
print(fruits)

fruits.pop(1)
print("............After Deleting elements at certain index............")
print(fruits)

# del method or del operation
del fruits[1]
# del fruits[-1]
print("............After Deleting elements at certain index............")
print(fruits)

# remove method

print("............After Removing elements............")
fruits.remove("kiwi")
print(fruits)
# fruits.remove("Papaya") # Papaya not available in the list it will generate an error

vegetables = ["Carrot",
    "Broccoli",
    "Corn",
    "Tomato",
    "Cucumber",
    "Spinach",
    "Potato",
    "Onion",
    "Carrot"
]
print(vegetables)
vegetables.remove("Carrot")
print("...Removing carrot at from first occurence...")
print(vegetables)

# method to add to list
# append insert extend

# method to delete from list
# pop del remove

