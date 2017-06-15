# Create a function named multiply that takes any number of arguments.
# Return the product (multiplied value) of all of the supplied arguments.
# The type of argument shouldn't matter.
# Slices might come in handy for this one.

def multiply(*args):
	if args.__len__() == 0:
		raise ValueError("please enter between 1 and many multiplicants separated by commas")
	elif args.__len__() == 1:
		return args[0]
	else:
		product = args[0] * args[1]
		for item in args[2:]:
			product = product * item
		return product

print(multiply(1))
print(multiply(3,5,2))
print(multiply())


	
