from navigation import ATOPIC_Y_EXIT, PROCEED_CLASS, PROCEED_TO_MENU_CLASS

#FIXME: plumb for pythonCartographer_delta
def depopulatingLists():

    def depopulateListBasics():

        print('''DEPOPULATING LISTS\n
          Modifying lists is a typical workflow in Python, items need to be added, and items need to be removed.
          We will explore how to depopulate lists with the pop() and remove() methods, and typical structures whereby these methods are
          used.\n''')
        
        proceed()
    
        print('''DEPOPULATING LIST WITH pop() and remove()\n
          The pop() method is a technique to remove the LAST ITEM of a list if no argument is added, or it can remove the item
          in a specific index if an argument is added, below is an example of how pop() is used in both manners.
          remove() removes the first occurrence of the value specified in its arg.\n
          
        the_list = ['dog', 'cat', 'bird', 'cat', 'whale', 'cat', 'dolphin']
        the_list.pop() #removes last item of list "dolphin
        print(the_list)
        the_list.pop(2) #removes item in the second index "bird"
        print(the_list)
        the_list.remove('cat') #removes the first "cat" from the list
        print(the_list)\n
          
        Proceed to run the code.\n''')
    
        proceed()
    
        the_list = ['dog', 'cat', 'bird', 'cat', 'whale', 'cat', 'dolphin']
        the_list.pop() #removes last item of list "dolphin
        print(the_list)
        the_list.pop(2) #removes item in the second index "bird"
        print(the_list)
        the_list.remove('cat') #removes the first "cat" from list
        print(the_list)

        proceedToMenu()

    def depopulateListWList():
        print('''REMOVING LIST ITEMS WITH ANOTHER LIST\n
        Items can be removed from one list by another list with remove(). This is done by iterating through one list
        and then searching for duplicate items in another list and removing them.
        like this:\n
        

        list26 = [1, 2, 3, 4, 5, 6]
        list62 = [2, 4, 6]

        for item26 in list26:
            if item26 in list62:
                list26.remove(item26)
        print(*list26)\n
          
        It will output 1 3 5 since * unpacker is used here
    
        Proceed to run the code''')

        proceed()

        # remove items from one list that are in another.

        list26 = [1, 2, 3, 4, 5, 6]
        list62 = [2, 4, 6]

        for item26 in list26:
            if item26 in list62:
                list26.remove(item26)
        print(*list26)

        proceedToMenu()

    def depopulateWListComp():

        print('''REMOVE WITH LIST COMPREHENSION\n
            FIXME: create list comprehension example. ''')

        proceedToMenu()

    while True:
        
        # declarations for depopulateLists() menu
        depopulate_menu =('''
        MENU - Depopulating Lists
        ........................................................................
        1: Depopulate List Basics
        2: Depopulate List with Another List
        3: Depopulate List with List Comprehension           
        OR ANY OTHER NUMBER TO EXIT.
        .........................................................................
        \n''')
        
        print(depopulate_menu)
        depopulate_selection = int(input('Select a Topic \n'))

        if depopulate_selection == 1:
            print(atopic)
            depopulateListBasics()
        elif depopulate_selection == 2:
            print(atopic)
            depopulateListWList()
        elif depopulate_selection == 3:
            print(atopic)
            depopulateWListComp
        else:
            print(ex)
            break 