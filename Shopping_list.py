print("Listmaker V1.0 \nBlackquill Nov/2017 \n")
print ("""
Tell me the things you would like to add to the list.
Type QUIT when you are done, type HELP for more info and commands.
""")

shopping_list = []

def list_help():
    print("""
Add items to the list by typing them and pressing ENTER.
Type SHOW to view the things you've added so far.
Type QUIT to stop entering items and view your completed list.
""")

def list_show():
    print(" ")
    for items_printout in shopping_list:
        print(items_printout.capitalize())
    print(" ")

def list_quit():
    print(" ")
    for items_printout in shopping_list:
        print(items_printout.capitalize())

def add_list():
    shopping_list.append(item)
    

while True:
    item = input("What should I add to your list: ").lower()
    if item == 'help':
        list_help()
        continue
    
    elif item == 'show':
        list_show()
        continue
    
    elif item == 'quit':
        list_quit()
        break
    
    else:
        if item in shopping_list:
            print(" ")
            print("That item is already on the list!\n")
            continue
        
        else:
            add_list()
            continue
