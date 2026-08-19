from navigation import ATOPIC_Y_EXIT, PROCEED_CLASS, PROCEED_TO_MENU_CLASS
# dicts.py covers dictionary operations. 
class DICTS_MENU():

    @staticmethod
    def dict_basics():
        # Covers basic dictionary structure and declaration
        print('''DICTIONARY BASICS\n
              Dictionaries are iterable structures that contain 2 components: key/value pairs.
              They are declared between {} such that:\n
              dictionaryName = {'keyName': 'valueName', ...}\n
              dictionaries can be comprised of any datatype; key is delimited by : and values are delimited by , .\n''')

        PROCEED_CLASS.proceed()

        print('''PRINTING DICTIONARIES\n
              There are a few common methods to print entire dictionaries.\n
              print(dictionaryName) and...\n
              with items() method
              print(dictionaryName.items())\n 
              with for loop
              for key, value in dictionaryName.items():
                print(key, value)\n
              
              The dictionary we will test these methods with is:\n
              
              dictionaryName = {'key0': 0, 'key1': 1, 'key2': 2}\n
              
              proceed to print the above dict with the above methods.''')
        
        PROCEED_CLASS.proceed()
        dictionaryName = {'key0': 0, 'key1': 1, 'key2': 2}

        print('With print(dictionaryName) method.\n', dictionaryName)

        print(f'with print(dictionaryName.items()) method\n', dictionaryName.items())

        print('''With:\n 
            for key, value in dictionaryName.items():\n
                print(key, value))\n''')
        for key, value in dictionaryName.items():
                print(key, value)

        PROCEED_CLASS.proceed()

        print('''PRINTING SPECIFIC KEYS AND VALUES\n
            Sometimes it is appropriate to print only part of a dictionary.
            The most common methods I use for this are .get() and the bracket method.\n''')
        
        print('''.get() METHOD\n
            The .get() method returns the value associated with a key/value pair such that:\n
            print(dictionaryName.get('keyname')) The code from earlier will be used to demonstrate
            this method\n''')
        print('''We will use the following code to get a value:\n
              print(dictionaryName.get('key1'))\n
              Proceed to get value with .get()\n''')

        PROCEED_CLASS.proceed()

        print(dictionaryName.get('key1'))

        print('The program has output "1".\n')

        PROCEED_CLASS.proceed()

        print('''BRACKET METHOD\n
            The bracket method prints the value of a key/value pair by:\n
            print(dictionaryName['key1'])\n
            The value returned will be 1.\n''')
        print('Proceed to run code.\n')

        PROCEED_CLASS.proceed()

        print(dictionaryName['key1'])

        print('''The program has output "1".\n
        This is the end to the module proceed to exit.''')

        PROCEED_TO_MENU_CLASS.proceedToMenu()

    @staticmethod
    def populating_dict():
        # populating dictionaries content here below
        print('''POPULATING DICTIONARIES\n
              In this module we will learn how to add key/value pairs to a dictionary using various methods.\n

              APPENDING DICTIONARY WITH NEW KEY/VALUE PAIR\n

              Adding a new key/value pair is easy. The method is:\n
              dict_name['keyname4'] = 4\n

              This will add the key/value pair to the last index of the dictionary.
              The code we will be working with to demonstrate this adding a new key\n
              dict_name = {'keyname0': 0, 'keyname1': 1}\n

              proceed to run code:\n
              ''')
        
        PROCEED_CLASS.proceed()

        dict_name = {'keyname0': 0, 'keyname1': 1}
        dict_name['keyname4'] = 4
        print(dict_name.items())

        print('''This method of appending dictionaries is hard coded on the back end.
            ''')
        
        PROCEED_CLASS.proceed()

        print ('''APPENDING A KEY/VALUE PAIR WITH USER INPUT\n
               
        Remember, keys are immutable so only values associated with keys can be appended.
        Sometimes values must be appended with user input. We will use the previous code:\n
               
        dict_name = {'keyname0': 0, 'keyname1': 1, 'keyname4': 4}\n
               
        to append keyname4 to any other associated value with the following code:\n
        
        new_value = input('Enter a new value for keyname4: )
        dict_name['keyname4'] = new_value
        print(dict_name.get('keyname4'))\n
               
        Proceed to run code. 
        ''')

        PROCEED_CLASS.proceed()

        new_value = input('Enter a new value for keyname4: ')
        dict_name['keyname4'] = new_value
        print(dict_name.get('keyname4'))

        print('''Remember keys are immutable, so to append a key the entire key/value pair must be deleted and redeclared.
            This is the end of this module, proceed to exit to Dictionaries menu.\n''')
        
        PROCEED_TO_MENU_CLASS.proceedToMenu()

    @staticmethod
    def dictOps():

        print('''DICT Methods include: .values(), .get(), .keys(), and .items()\n
        dictName.values() - returns all values stored in dict.\n
        dictName.get('keyName') - gets all values associated with key.\n
        dictName.items() - gets all K/V pairs.\n
        'keyname' in aDict - looks for a key in a dict, if not returns False.\n
        dictName.keys() - gets all keys in dictionary.\n

        the dictionary we'll be using to demonstrate the methods

        # dicts containing med staff info
                sc_1: dict = {'name': 'Dr. Lingard', 'on_duty': False, 'Location': "off campus" }
                sc_2: dict = {'name': 'Dr. Morley', 'on_duty': True, 'Location': 'A-29'}
                sc_3: dict = {'name': 'Dr. Kuhlman', 'on_duty': True, 'Location': 'Reception'}
        
                # list of medstaff containing dicts
                san_cristobal_medstaff: list = [sc_1, sc_2, sc_3]

        Proceed to continue\n''')
        
        PROCEED_CLASS.proceed()

        # dicts containing med staff info
        sc_1: dict = {'name': 'Dr. Lingard', 'on_duty': False, 'Location': "off campus" }
        sc_2: dict = {'name': 'Dr. Morley', 'on_duty': True, 'Location': 'A-29'}
        sc_3: dict = {'name': 'Dr. Kuhlman', 'on_duty': True, 'Location': 'Reception'}

        # list of medstaff containing dicts
        san_cristobal_medstaff: list = [sc_1, sc_2, sc_3]

        print('''GETTING KEYS WITH .get()\n

        First since we are working with a list of dicts, we need to access the index and extract
        its name with .get()
        
        print(san_cristobal_medstaff[0].get('name')) # prints 'Dr. Lingard'
        
                # prints all med staff info
                for staff in san_cristobal_medstaff:
                    print(staff.get('name'))
                    print(staff.get('on_duty'))
                    print(staff.get('Location'))

        proceed to run code\n''')

        PROCEED_CLASS.proceed()

        print(san_cristobal_medstaff[0].get('name') + '\n')

        for staff in san_cristobal_medstaff:
            print(staff.get('name'))
            print(staff.get('on_duty'))
            print(staff.get('Location') + '\n')

        PROCEED_CLASS.proceed()

        print('''Getting values with .values()\n

        In this simplified operation, we see how values() extracts the values associated with sc_2.

        print(san_cristobal_medstaff[1].values())
        
        This example will pull all values associated with staff in san_cristobal_medstaff

        for staff in san_cristobal_medstaff:
                print(staff.values())
                
        proceed to run these codes.''')


        PROCEED_CLASS.proceed()

        print((san_cristobal_medstaff[1].values()), '\n')
        
        for staff in san_cristobal_medstaff:
            print(staff.values(), '\n')

        PROCEED_CLASS.proceed()

        print('''EXTRACTING DICTS WITH .items()\n

        items will pull all K/V pairs in a dict. This is the example we will use:

        print(san_cristobal_medstaff[2].items()) # pulls all K/V from sc_3.

        procced to run code:\n''')

        PROCEED_CLASS.proceed()

        print((san_cristobal_medstaff[2].items()), '\n')

        PROCEED_CLASS.proceed()

        print('''FINDING KEYS WITH "in" KEYWORD.\n
        
        "in" can be used to determine if a key is inside a dictionary such that:

        for staff in san_cristobal_medstaff:
                    print('san_cristobal_safe' in staff)

        This will of course print False because the key san_cristobal_medstaff does not exist
        and there is a Xenomorph loose in the facility.

        proceed to run the code.\n''')

        PROCEED_CLASS.proceed()

        for staff in san_cristobal_medstaff:
            print(('san_cristobal_safe' in staff), '\n')

        PROCEED_CLASS.proceed()

        print('''GETTING KEYS WITH .keys()\n
            Using .keys() will extract all the keys from a dictionary such that:\n
            for staff in san_cristobal_medstaff:
                        print(staff.keys())\n
            This will print all keys associated with the dictionaries in san_cristobal_medstaff since
            the list stores dictionaries.\n
            
            Proceed to run program\n''')

        PROCEED_CLASS.proceed()
        

        for staff in san_cristobal_medstaff:
            print((staff.keys()), '\n')

        PROCEED_TO_MENU_CLASS.proceedToMenu()

    @staticmethod
    def runDictMenu():
        while True:
            dict_menu = '''MENU - Dictionaries
            ........................................................................
            1: Dictionary Basics
            2: Populating Dictionary
            3: Dictionary Methods .get(), .keys(), .values(),.items()       
            OR ANY OTHER NUMBER TO EXIT.
            .........................................................................\n)'''

            print(dict_menu)
            dict_selection = int(input("Select a topic:\n "))
            if dict_selection == 1:
                ATOPIC_Y_EXIT.atopic()
                DICTS_MENU.dict_basics()
            elif dict_selection == 2:
                ATOPIC_Y_EXIT.atopic()
                DICTS_MENU.populating_dict()
                # finish depopulating dict and iterating through dict.
            elif dict_selection == 3:
                ATOPIC_Y_EXIT.atopic()
                DICTS_MENU.dictOps() 
            else:
                ATOPIC_Y_EXIT.exiting()
                return