#word guessing game
#given a mystery word, and it's length, your goal is to guess the entire word, before you run out of guesses.

#build a guess dictionary
#pick difficulty (sets number of guesses)
#pick word from dictionary
#display the word as underscores to show length


import random

#create a dictionary of works the player can choose from
#dictionary = ["serendipidy", "enterprise", "cat"]
dictionary = ["cat", "dog", "seal", "elephant", "fox"]
guesses = 0
word_list = []
shadow_list = []
letter_guess = ""

#find all occurences of an element in an array
def indices(lst, element):
    result = []
    offset = -1
    while True:
        try:
            offset = lst.index(element, offset+1)
        except ValueError:
            return result
        result.append(offset)
		
#print list
def print_list(list):
	for letter in list:
		print(letter, end='')
	print("\n")
		
print("Welcome to HangMan")
print("Choose your difficulty")
print("Type 1 for Easy")
print("Type 2 for Hard")
difficulty = input("> ")
try:
    difficulty = int(difficulty)
except ValueError:
    print("bad or no value")
except TypeError:
    print("bad value")
else:
    if difficulty != "1" and difficulty != "2": #input is a string
        print ("Bad value entered")
    else:
        difficulty = int(difficulty)
print("Thanks, you chose {}".format(difficulty)) 

print("Picking word")
file = open("dictionary.txt","r")
lines = file.read().splitlines()
word = random.choice(lines)

#set number of guesses based on word length
guesses = int(len(word)*5/difficulty)

print("Your word is: ")
print("_"*len(word))
print("You have " + str(guesses) + " guesses")

#convert picked word to a list
word_list = list(word)
#create a list equal in length to letters and filled with underscores, one for each letter
shadow_string = '_'*len(word)
shadow_list = list(shadow_string)

def check_win(word_list, shadow_list):
	if word_list == shadow_list:
		debug()
		return true
	else:
		return false

def write_shadow_list(shadow_list, letter_guess, indices):
	for position in indices:
		shadow_list[position] = letter_guess
		
def debug():
	print("debug message:")
	print(letter_guess)
	print(word_list)
	print(shadow_list)
	print("guesses left: {}".format(str(guesses)))
	
#keep track of letters
#display the guessed letters in their right positions
#keep track of guesses
#win condition
	# Guesses > 0 and shadow array and original word array are the same
#lose condition
	# Guesses == 0 and shadow array and original word array are not the same

while True:
	#debug()
#user guesses letter
	letter_guess = input("Enter a letter as your guess: > ")
    # what if entered thing is not a letter?
        # way to exit
	matches = indices(word_list, letter_guess)
	# if entered letter is in the word
	if len(matches) > 0:
    # display position(s) in the word
		# write the guesses to the shadow array
		write_shadow_list(shadow_list, letter_guess, matches)
		# print the shadow array
		print_list(shadow_list)
		# Check win condition
		if word_list == shadow_list:
			debug()
			print("You win")
			break
        # decrement guess counter
		guesses -= 1
		print("You have {} guesses left".format(str(guesses)))
		# if guess counter == 0 
		if guesses == 0:
				# lose
				print("you lose")
				break
    # else 
	else:
		print_list(shadow_list)
		 # decrement guess counter
		guesses -= 1
		print("You have {} guesses left".format(str(guesses)))
		# if guess counter == 0 
		if guesses == 0:
			# lose
			print("you lose")
			break

# each line shows remaining letters to be guessed, letters already guessed, the current state of the word
