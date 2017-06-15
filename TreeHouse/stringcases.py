#Create a function named stringcases that takes a single string but returns a tuple of different string formats. The formats should be:
#All uppercase
#All lowercase
#Titlecased (first letter of each word is capitalized)
#Reversed

def stringcases(str):
	stringcases = (str.upper(), str.lower(), str.title(), str[::-1])
	return stringcases
	
print(stringcases("Hello there!"))