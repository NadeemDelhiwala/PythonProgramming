# some more list methods
# count
# sort method
# sorted function
# reverse
# clear
# copy

fruits = [
    "Apple",
    "Banana",
    "Orange",
    "Mango",
    "Grapes",
    "Pineapple",
    "Strawberry",
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

print("...Our Fruits List...")
print(fruits)
print(f"............Frequency(count())............ :{fruits.count('Apple')}")

fruits.sort();
print("Sorting Alphabetically orders : ")
print(fruits)

numbers = [3, 5, 1, 9, 10]
print("......Before sorting.....")
print(numbers)

numbers.sort()
print("......After sorting.....")
print(numbers)

# sorted function - whenever you do not want to sort your list but print it in sorted order
num_sortedfunc = [34, 1, 45, 9, 12, 5]
print(num_sortedfunc)
print(".......Sorted Function...");
print(sorted(num_sortedfunc))
print("....Original List....")
print(num_sortedfunc)

# clear deletes all elements from the list
num_sortedfunc.clear();
print(num_sortedfunc)

num1 = [1, 4, 2, 9, 3, 8, 5]
num1_copy = num1
print(num1)
print(num1_copy)

print("...Reversing the elements of list...")
num1.reverse();
print(num1);
