'''
Create a function named combo that takes two ordered iterables.
These could be tuples, lists, strings, whatever.
Your function should return a list of tuples. Each tuple should hold the first item in each iterable, then the second set, then the third, and so on. Assume the iterables will be the same length.
'''

# combo([1, 2, 3], 'abc')
# Output:
# [(1, 'a'), (2, 'b'), (3, 'c')]

def combo(iter1, iter2):
	output = []
	if (len(iter1) != len(iter2)):
		raise ValueError("you must supply two iterables of equal length")
	end = len(iter1)
	count = 0
	while count < end:
		output.append((iter1[count],iter2[count]))
		count += 1
	return output


# nicer way of doing it

def combo1(iter1, iter2):
  tup_list = []

  
  for count in range(0, len(iter1)):
    tup = tuple((iter1[count], iter2[count]))
    tup_list.append(tup)

  return tup_list



print(combo([1, 2, 3], 'abc'))

print(combo1([1, 2, 3], 'abc'))

