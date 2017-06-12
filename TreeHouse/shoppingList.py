# run the script to start it
# put new things into the list, one at a time
print("Welcome to your shopping list")
list = []
item = ""

def print_list(list):
    for item in list:
        print(item)

def help():
    print("Enter LIST to print the list")
    print("Enter HELP to show this help menu")
    print("Enter STOP to quit and print the list")

help()
while True:
    item = input("Please enter an item: ")
    if item == "LIST":
        print_list(list)
    elif item == "HELP":
        help()
    elif item == "STOP":
        print_list(list)
        break
    else:
        list.append(item)

# enter the word DONE to quit
# once quit, show everything on the list

