from navigation import ATOPIC_Y_EXIT, PROCEED_CLASS, PROCEED_TO_MENU_CLASS

class DEPOPULATE_LIST_MENU():

    @staticmethod
    def depopulateListBasics():

        print('''DEPOPULATING LISTS\n
          Modifying lists is a typical workflow in Python, items need to be added, and items need to be removed.
          We will explore how to depopulate lists with the pop(), del, and remove() methods, and typical structures whereby these methods are
          used.\n''')
        
        PROCEED_CLASS.proceed()
    
        print('''DEPOPULATING LIST WITH .pop() and .remove()\n
          .pop(index) returns value\n
          .remove(value) returns none\n
          del iterable[index]\n

          Remember: .pop(index) - returns value, .remove(value) returns none. del is a command.\n
          
        the_list = ['dog', 'cat', 'bird', 'cat', 'whale', 'cat', 'dolphin']
        the_list.pop() #removes last item of list "dolphin"
        print(the_list)
        the_list.pop(2) #removes the value 'bird' at the the second index
        print(the_list)
        the_list.remove('cat') #removes the first "cat" from the list
        del the_list[3] deletes last 'cat' value
        print(the_list)\n

        list will finally print as ['dog', 'cat', 'whale']
          
        Proceed to run the code.\n''')
    
        PROCEED_CLASS.proceed()
    
        the_list = ['dog', 'cat', 'bird', 'cat', 'whale', 'cat', 'dolphin']
        the_list.pop() #removes last item of list "dolphin
        print(the_list)
        the_list.pop(2) #removes item in the second index "bird"
        print(the_list)
        the_list.remove('cat') #removes the first "cat" from list
        del the_list[3] # removes last 'cat' value
        print(the_list)
       

        PROCEED_TO_MENU_CLASS.proceedToMenu()

    @staticmethod
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

        PROCEED_CLASS.proceed()

        # remove items from one list that are in another.

        list26 = [1, 2, 3, 4, 5, 6]
        list62 = [2, 4, 6]

        for item26 in list26:
            if item26 in list62:
                list26.remove(item26)
        print(*list26)

        PROCEED_TO_MENU_CLASS.proceedToMenu()

    @staticmethod
    def removeWSlice():

        print('''Since lists are iterables, lists can be depopulated with a slice such that:\n
            alist: list = ['brad', 'leo', 'sandy', 'timothy', 'sam']
        
            del alist[2:-1] # removes 'sandy' and 'timothy'
        
            print(*alist)\n
            
            Proceed to run the code!\n''')

        PROCEED_CLASS.proceed()
        
        alist: list = ['brad', 'leo', 'sandy', 'timothy', 'sam']

        del alist[2:-1] # removes 'sandy' and 'timothy'

        print(*alist)

        PROCEED_TO_MENU_CLASS.proceedToMenu()

    @staticmethod
    def runDepopulateListMenu():
        while True:
        
            # declarations for depopulateLists() menu
            depopulate_menu =('''
            MENU - Depopulating Lists
            ........................................................................
            1: Depopulate List Basics
            2: Depopulate List with Another List
            3: Depopulate with del[slice]          
            OR ANY OTHER NUMBER TO EXIT.
            .........................................................................
            \n''')
        
            print(depopulate_menu)
            depopulate_selection = int(input('Select a Topic \n'))

            if depopulate_selection == 1:
                ATOPIC_Y_EXIT.atopic()
                DEPOPULATE_LIST_MENU.depopulateListBasics()
            elif depopulate_selection == 2:
                ATOPIC_Y_EXIT.atopic()
                DEPOPULATE_LIST_MENU.depopulateListWList()
            elif depopulate_selection == 3:
                ATOPIC_Y_EXIT.atopic()
                DEPOPULATE_LIST_MENU.removeWSlice()
            else:
                ATOPIC_Y_EXIT.exiting()
                return 