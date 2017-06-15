# You can also do it with recursion:

def reverse(text):
    if len(text) <= 1:
        return text

    return reverse(text[1:]) + text[0]

'''
And a simple example for the string hello:

   reverse(hello)
 = reverse(ello) + h           # The recursive step
 = reverse(llo) + e + h
 = reverse(lo) + l + e + h
 = reverse(o) + l + l + e + h  # Base case
 = o + l + l + e + h
 = olleh
'''


