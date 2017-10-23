# Write a program that asks the user for two lists of numbers separated by commas and prints out a list of numbers that appear in both lists (no duplicates). Make sure the program works when the lists have different lengths.

#take in data
#(validate data)
#parse input into a list
#convert into set
#intersect sets

list1 = input("Enter list 1: ")
list2 = input("Enter list 2: ")
list1 = list1.split(",")
list2 = list2.split(",")

print(set(list1).intersection(set(list2)))

#test
