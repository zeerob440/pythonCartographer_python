from navigation import ATOPIC_Y_EXIT, PROCEED_CLASS, PROCEED_TO_MENU_CLASS
     
# lists.py covers examples of list operations. 
class LISTS_MENU():

    @staticmethod
    def populateLists():
        print('''
        POPULATING LISTS\n
        Lists are a great way to store data. Lists can store virtually any Python data type.
        They can be populated via hardcoding values into them such that:\n
        my_list =['dog', 'cat']
        their_list = [2 ,'cherry','mouse']\n
        In Python data types do not need to be the same to create a list like in many other languages.
        ''')
    
        PROCEED_CLASS.proceed()

        print('''
        POPULATING LISTS WITH .append()\n
        .append() is a method for adding an item to the last index of a list. It expects an argument inside the().
        The argument is the input variable intended to be added to the list such that:\n
        dog_list =['Rico']
        new_dog = input('Enter a dog to list: ')\n
        dog_list.append(new_dog)
        print(dog_list)
        ['Rico', 'Mia']\n
        Proceed to run this example: You'll need to input a name.\n
        ''')
    
        PROCEED_CLASS.proceed()

        dog_list = ['Rico', 'Mia']
        new_dog = input("Enter a new dog: ")
        dog_list.append(new_dog)
        print(dog_list)
    
        PROCEED_TO_MENU_CLASS.proceedToMenu()

    @staticmethod
    def populateListForLoop():

        print('''
        POPULATING LIST WITH FOR LOOP\n
        Lists are often populated with loops the example below is:\n
          
        user_things = [] # declare empty list.
        for i in range(3):# initiate for loop.
            user_thing_input = input('Enter a anything: ')# declare user input variable.
            user_things.append(user_thing_input)# use .append() method to populate the list
        print(user_things)# print raw list.\n
          
        Proceed to try it. The code will allow you to input 3 items.\n
        ''')
    
        PROCEED_CLASS.proceed()

        # Below is an example of populating a list with the .append() method.
        user_things = [] # declare empty list.
        for i in range(3):# initiate for loop.
            user_thing_input = input('Enter anything: ')# declare user input variable.
            user_things.append(user_thing_input)# use .append() method to populate the list
        print(user_things)# print raw list.

        PROCEED_TO_MENU_CLASS.proceedToMenu()

    @staticmethod
    def populateListInsert():

        print('''POPULATING LIST WITH insert()\n
          Another way to populate a list is with the insert() method.
          insert() expects two args, insert('index_to_insert_at, 'element_you_need_to_insert) such  that:\n
          cat_list = ['tabby', 'siamese', 'persian']\n
          cat_list.insert(1, 'main coon')\n
          print(cat_list)\n
          
          proceed to run this code.\n
          ''')
    
        PROCEED_CLASS.proceed()

        cat_list = ['tabby', 'siamese', 'persian']
        cat_list.insert(1, 'main coon')
        print (cat_list)

        PROCEED_TO_MENU_CLASS.proceedToMenu()

    @staticmethod
    def populateListWhileLoop():
        print('''
        POPULATING LIST WITH WHILE LOOP\n
        It is also possible to populate a list with an while loop. Below is an example of how this is achieved.\n
        another_list = [] #declare empty list
        append_list = True
        while append_list:
            list_apendenator = input('Enter an item to list: ')
            another_list.append(list_apendenator)
            sentinel_prompt = input('Would you like to add another item? Enter "y" or "n": ')
                if sentinel_prompt == ('y'):      
                    append_list = True
                else: append_list = False
        print(*another_list)# * IS USED FOR UNPACKING LISTS IT REMOVES ALL THE COMMAS AND BRACKETS.
        Below this code will prompt you to populate a list until you input 'n'\n
        ''')

        PROCEED_CLASS.proceed()

        another_list = [] #declare empty list
        append_list = True
        while append_list:
            list_apendenator = input('Enter an item to list: \n')
            another_list.append(list_apendenator)
            sentinel_prompt = input('Would you like to add another item? Enter "y" or "n": \n')
            if sentinel_prompt == ('y'):      
                append_list = True
            else: append_list = False
        print('You entered\n')
        print(*another_list)# * is used for argument unpacking it removes commas and brackets.

        PROCEED_TO_MENU_CLASS.proceedToMenu()

    @staticmethod
    def populateListSplit():
        print('''
        POPULATING LIST WITH .split()\n
        WARNING: THIS INPUT METHOD SHOULD NOT BE USED AS IT IS POOR PROGRAMMING FORM AND CONFUSES USERS.\n

        Lists can be created using the .split() method. However, it is important to warn the user
        that this method of input is being used. The .split() method uses space to separate several items in a list
        the list is then created when the user presses enter.
        
        Below is an example of how this method is used for user input.\n
          
        enter_items = input('enter an item separated by space ')# input variable
        items = enter_items.split() create a variable to contain the items once split into a list the var becomes the list.
        print(items) # items is now a list\n.
        Now you try:\n''')

        enter_items = input('Enter an item separated by space: ')
        items = enter_items.split()
        print(items)

        PROCEED_TO_MENU_CLASS.proceedToMenu()

    @staticmethod
    def populateListConcat():

        print('''JOINING LISTS WITH CONCATENATION\n
        Another method of populating lists is to concatenate them. Such that you simply add the list together in another variable.
        since you are concatenating two list the new variable is also list such that:\n
         A simple program demonstrating how to concatenate lists.

        list1 = [1, 2 , 3]
        listA = ['a','b','c']\n

        combined_list = (list1 + listA)\n

        print(combined_list)\n

        Proceed to run this program, it will output [1, 2 ,3, 'a', 'b', 'c']\n''')
    
        PROCEED_CLASS.proceed()

        list1 = [1, 2 , 3]
        listA = ['a','b','c']

        combined_list = (list1 + listA)

        print(combined_list)

        PROCEED_CLASS.proceed()

        print('''.split()\n
    .split() can create a list using a string and a separator value such that:\n

    str4 = 'many dogs live in my house|Rico is a Standard Schnauzer|Mia is a Yukon Whaling Shepard.'
    
    # produces a three element list starting at each "|".
    print(str4.split('|'))\n
    
    Proceed to run this code.\n''')

        PROCEED_CLASS.proceed()

        str4 = 'many dogs live in my house|Rico is a Standard Schnauzer|Mia is a Yukon Whaling Shepard.'

        # produces a three element list starting at each "|".
        print(str4.split('|')) 

        PROCEED_TO_MENU_CLASS.proceedToMenu()
        
    @staticmethod
    def populateWExtend():

        print('''.extend()\n 
    .extend is a useful method for adding elements to a list. 
    The use case is simple: suppose you need to add two elements to a list from another list, but if you add those elements as .append() THE
    ENTIRE LIST becomes a single element in your original list.\n
        
    .extend() can take a list with multiple elements as an arg, then iteratively load each element into the list as its own element.\n
        
    Observe this example:\n

    bears: list = ['polar', 'grizzly', 'wachbar']
    colors: list = ['red', 'blue']
        
    bears.extend(colors) # takes each element from colors and adds it as an independent element in bears.
    print(bears)\n
        
    Proceed to run this example.\n''')

        PROCEED_CLASS.proceed()

        bears: list = ['polar', 'grizzly', 'wachbar']
        colors: list = ['red', 'blue']

        bears.extend(colors)
        print(f'{bears} \n')# prints bears and colors as separate elements.

        PROCEED_CLASS.proceed()

        print('''Whereas .append() will add a single element to the last indice in a list. Such that:\n
        
        birds: list = ['toucan', 'loro', 'flamingo', 'pelican']
        space_stations: list = ['Death Star', 'Citadel', 'Sevastopol', 'Sky Lab']
        
        birds.append(space_stations) # prints elements in birds, but appends entire list of space_stations in last element of birds.
        
        print(birds)\n
        proceed to run this code!
        ''')
        PROCEED_CLASS.proceed()

        birds: list = ['toucan', 'loro', 'flamingo', 'pelican']
        space_stations: list = ['Death Star', 'Citadel', 'Sevastopol', 'Sky Lab']

        birds.append(space_stations) # prints elements in birds, but appends entire list of space_stations in last element of birds.

        print(f'{birds} \n') 

        PROCEED_TO_MENU_CLASS.proceedToMenu()

    @staticmethod
    
    def comprehensions():

        print('''LIST COMPREHENSIONS\n
    More like list incomprehensions, am I rite? List comprehension are a way to produce a list using elements from another list with conditional logic baked in
    . They are essentially filters for one list to produce another list.
    They can be useful, but the syntax is like how Yoda's speaks and can very quickly become virtually unreadable.\n

    Remember, "write it you must, so others can maintain it.'
    
    While comprehensions can be 'elegant' I feel readability and maintainability exceed the usefulness of 'cute code'.\n ''')

        PROCEED_CLASS.proceed()

        print('''Structure of a Comprehension\n
    A list comprehension generates a new list from another iterable. They always use for loops so,\n

    IT IS IMPORTANT TO BEGIN READING FORM THE 'for' STATEMENT IN THE MIDDLE OF THE EXPRESSION!

    generated list = [varYouWant for elementInExistingIterable in existingIterable]

    or 

    new_list = [expression for item in iterable]

    or

    [what_to_store for item in iterable if condition]\n 

    As you can see this kind of misheagoss can get convoluted very quickly if you are not careful.\n''')

        PROCEED_CLASS.proceed()

        print('''let's look at our example code below:
    # existing list
    nums = [10, 10, 10]
    # new list built with list comprehension
    zeroes =[num - 10 for num in nums]
    print (zeroes)# returns a list with three 0s
    print()\n    
    
    The code is literally read as:\n
    "for number in nums, num - 10"
    proceed to run it\n''')

        # existing list
        nums = [10, 10, 10]
        # new list built with list comprehension
        zeroes =[num - 10 for num in nums]
        print (f'{zeroes}\n')

        PROCEED_CLASS.proceed()

        print('''An equal, but more readable code for this would be:\n
        
        smartzeros = []
        for num in nums:
            minus10 = (num -10)
            smartzeros.append(minus10)
        print(smartzeros)\n
        
        proceed to try it\n''')

        PROCEED_CLASS.proceed()

        smartzeros: list = []
        for num in nums:
            minus10 = (num -10)
            smartzeros.append(minus10)
        print(f'{smartzeros} equal output as the zeros list comprehension list.\n')

        PROCEED_CLASS.proceed()

#FIXME: add the cats example here.
        print('''NEXT EXAMPLE''')
    @staticmethod
    def runListsMenu():

        while True:
        
            # declarations for populateLists() menu
            populate_list_menu =('''
            MENU - 
            ........................................................................
            1: List Population .append()
            2: List Population for loop
            3: List Population insert()
            4: List Population While Loop
            5: List Population split()
            6: Joining lists Concatenation and .split()
            7. List Population using .extend() vs .append()
            8. List Comprehension Structures           
            OR ANY OTHER NUMBER TO EXIT.
            .........................................................................
            \n''')
        
            print(populate_list_menu)
            populate_list_selection = int(input('Select a Topic \n'))

            if populate_list_selection == 1:
                ATOPIC_Y_EXIT.atopic()
                LISTS_MENU.populateLists()
            elif populate_list_selection == 2:
                ATOPIC_Y_EXIT.atopic()
                LISTS_MENU.populateListForLoop()
            elif populate_list_selection == 3:
                ATOPIC_Y_EXIT.atopic()
                LISTS_MENU.populateListInsert()
            elif populate_list_selection == 4:
                ATOPIC_Y_EXIT.atopic()
                LISTS_MENU.populateListWhileLoop()
            elif populate_list_selection == 5:
                ATOPIC_Y_EXIT.atopic()
                LISTS_MENU.populateListSplit()
            elif populate_list_selection == 6:
                ATOPIC_Y_EXIT.atopic()
                LISTS_MENU.populateListConcat()
            elif populate_list_selection == 7:
                ATOPIC_Y_EXIT.atopic()
                LISTS_MENU.populateWExtend()
            elif populate_list_selection == 8:
                ATOPIC_Y_EXIT.atopic()
                LISTS_MENU.comprehensions()
            else:
                ATOPIC_Y_EXIT.exiting()
                return        

