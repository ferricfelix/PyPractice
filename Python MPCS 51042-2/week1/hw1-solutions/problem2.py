# Get user input
str1 = input("Enter list 1: ")
str2 = input("Enter list 2: ")

# Convert strings to lists of integers
list1 = [int(x) for x in str1.split(",")]
list2 = [int(x) for x in str2.split(",")]

# Convert lists to sets, find intersection, convert back to list
common = list(set(list1) & set(list2))
print(common)
