shopping_list = []

def show_help():
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'SHOW' to see your current shopping list.
""")
    
    
def add_to_list(item):
    shopping_list.append(item)
    print("You've just added {} to the shopping cart! You currently have {} items in your list.".format(item, len(shopping_list)))
    

def show_list():
    print("Here's your list:")
    for item in shopping_list:
        print(item)


show_help()

while True:
    new_item = input("> ")
    
    if new_item == "DONE":
        break
    elif new_item == "HELP":
        show_help()
        continue #these continues say to go back to the while true part when done.
    elif new_item == "SHOW":
        show_list()
        continue  
    add_to_list(new_item)
    #I can remove the continue lines if i move this into an else statement
#else add_to_list(new_item)
show_list()