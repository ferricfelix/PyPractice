word = "serendipidy"
letters = list(word)
print(letters)
letter = str(input("enter the letter you want to find> "))

def indices(lst, element):
    result = []
    offset = -1
    while True:
        try:
            offset = lst.index(element, offset+1)
        except ValueError:
            return result
        result.append(offset)
		
print(indices(letters,letter))