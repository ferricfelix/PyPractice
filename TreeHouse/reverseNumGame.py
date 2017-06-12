# the goal of the game is for the computer to guess at the number that we generate for it
import random

# ask the user for input within a certain range
def user_input():
    mystery = input("Please a pick a number between 1 and 100 inclusive> ")
    return mystery

number = user_input()
try:
    number = int(number)
except TypeError:
    print("You should enter an integer")
else:
    print("You have entered " + str(number))

# computer generates a guess within the defined range
high = 100
low = 0
guess = random.randint(low, high)

def print_range():
    return ("Range is {},{}.".format(low,high))
    
while guess != number:
    if guess > number:
        #print("high")
        high = guess - 1
        print("Computer guessed {}, too high.".format(guess) + " " + print_range())
        guess = random.randint(low, high)
        continue
    elif guess < number:
        #print("low")
        low = guess +1 
        print("Computer guessed {}, too low.".format(guess) + " " + print_range())
        guess = random.randint(low, high)
        continue
    else:
        break
print("{} has been found by guessing {}".format(number,guess))
    
# if the guess is too low, computer generates a new guess
# if the guess is too high, computer generates a new guess
# game is over when the computer lands on the correct number
