#unpacking a dictionary
>>> my_dict = {'name': 'Kenneth'}
>>> "Hi, my name is {name}!".format(**my_dict)
"Hi, my name is Kenneth!"

#packing a dictionary
>>> def packing(**kwargs):
...     print(len(kwargs))
>>> packing(name="Kenneth")
1


New Terms

.update() - Pass in a dictionary of keys and values to create or update in a single step.

You can override a single key by assigning a new value to it. And you can delete a key by using del and the key's name.

Try on your own!

I didn't show them but there are a few other handy dictionary methods you might want to try.

.pop(<key>) - like lists, dicts have .pop(). It'll return the key's value to you and then delete the key.
.popitem() - similar to .pop() but instead of returning just the value, returns you a tuple (more in the next stage!) with the key and the value. Also, this doesn't take any arguments, you get a random key/value pair!
.clear() - need to quickly empty out a dictionary? This method is your tool of choice, then.

## iterating over dictionaries

players = {"player1":"Gene", "player2":"Nina"}
for player in players:
	print(player) #prints the key of each item
	
for player in players:
	print(players[player]) #prints the value associated with each key

## iterating using methods

>>> for key in dictionary.keys():
...     print(key)
... 
player1
name
player2

>>> for value in dictionary.values():
...     print(value)
... 
Gene
Nina
Nina

>>> for item in dictionary.items():
...     print(item)
... 
('player1', 'Gene')
('name', 'Nina')
('player2', 'Nina')