#I need you to make a function named word_count.
#It should accept a single argument which will be a string.
#The function needs to return a dictionary. 
#The keys in the dictionary will be each of the words in the string, lowercased.
#The values will be how many times that particular word appears in the string.


# E.g. word_count("I do not like it Sam I Am") gets back a dictionary like:
# {'i': 2, 'do': 1, 'it': 1, 'sam': 1, 'like': 1, 'not': 1, 'am': 1}
# Lowercase the string to make it easier.

someString = "Spiderman, spiderman, does whatever a spiderman wants"
def word_count(inputString):
	outputDictionary = {} #keys are each of the words: values are how many times a particular word appears in the string
	#break up the string into words
	wordList = inputString.lower().split() #does not get rid of punctuation
	#for each word in a string
		#if a key with that word already exits, add one to the value
		#else create a key:value pair with value initialized to 0
	for word in wordList:
		if word in outputDictionary:
			outputDictionary[word] += 1
		else:
			outputDictionary.update({word:1})
	return outputDictionary

print(word_count(someString))

