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
# variable f will still exist outside the scope, but is closed
# so if you want to reopen the file, you will need to open it again
# for more info, look at the standard library at docs.python.org
with open('data.csv', 'r') as f:
	#do some work with the file

# Context managers require that a class have two defined methods:
__enter__()
__exit__()

with obj as:
	...
# is roughly equivalent to
try:
	x = obj.__enter__()
	...
finally
	obj.__exit__()

# usually takes no arguments and returs self
__enter__() 

# decimal allows to you to go more precise than float
from math import pi
print(pi)
# vs
from decimal import Decimal, localcontext

with localcontext() as ctx:
	ctx.prec = 100
	d = Decimal('1')/Decimal('7')
	print(d)
	# get 100 points of precision



