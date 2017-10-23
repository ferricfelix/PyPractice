# Given a file with a single column of numbers, write a program that calculates the mean, sample standard deviation, and the mode of the numbers
# The name of the file should be given as the first command-line argument which can be accessed using sys.argv[1]
# You are not allowed to use any standard-library or third-party packages that perform these calculations automatically
# However, you may use data structures defined in the collections package from the standard library if you so wish
#
# Example file:
# 9 5 14 5 20 7
#
# Expected output:
#    Mean: 10.0
#    Standard deviation: 5.932958789676531
#    Mode: 5
#
# read file
# process file in to a data structure of some sort
# create functions
#############
import sys
import math
import collections

nums = []
with open('input', 'r') as f:
	for line in f:
		nums.append(int(line))


def mean(nums):
	return sum(nums) / len(nums)


def stddev(nums):

	sum = 0
	for num in nums:
		sum += (num - mean(nums))**2
	print(sum)
	return math.sqrt((1 / (len(nums) - 1)) * sum)


def mode(nums):
	s = set(nums)
	d = dict()
	for item in s:
		d.update({item: 0})
	for num in nums:
		d[num] += 1
	sd = sorted(d.items(), key = lambda x: x[1], reverse = True)
	return sd[0][1]



print(mean(nums))
print(stddev(nums))
print(mode(nums))
