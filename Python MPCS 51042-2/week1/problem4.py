'''
Write a program that determines all six-digit numbers SLAYER
(where each letter stands for the digit in the position shown)
where the following equation true: SLAYER + SLAYER + SLAYER = LAYERS.
For example, one number which satisfies this is 142857.
The program should print out the above equation for each solution.

Sample output:
   142857 + 142857 + 142857 = 428571
   ...
HINT: Although there may be some way to methodically solve the puzzle,
it is by far easier to just brute force it by checking every single possibility.
The itertools.permutations function can give you each permutation of the digits 0-9.
'''
#numbers should be in order 234561

output = []
for x in range(111111,999999):
	l = [int(d) for d in str(x)]
	sumList = [l[1], l[2], l[3], l[4], l[5], l[0]]
	if x*3 == int(''.join(str(digit) for digit in sumList)):
		output.append(x)
print(output)






