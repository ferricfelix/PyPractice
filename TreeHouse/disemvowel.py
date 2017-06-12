#don't iterate over a list as you are removing items from it!
def disemvowel(word):
    vowels = "aeiouAEIOU"
    my_list = list(word)
    for char in word:
        if char in vowels:
            my_list.remove(char)
    new_word = ''.join(my_list)
    print(new_word)
	
	


#disemvowel("apple")
#disemvowel("APPLE")
disemvowel("aeiouAEIOUcandy")
