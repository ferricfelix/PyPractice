# at the end of the block the file is automatically closed
# ie you don't have to do a f.close() and worry about files not getting closed if things break
with open (...) as f:
		f.readline()
		...

#
with lock:
	x += 1

# the finally statement will execute no matter what errors you get
try:
	f = open('data.csv', 'r')
	# do some work with the file
finally:
	f.close()

#example of using with to not require the finally clause
with open('data.csv', 'r') as f:
	#do some work with the file

