from navigation import ATOPIC_Y_EXIT, PROCEED_CLASS, PROCEED_TO_MENU_CLASS
     
class BASICS_MENU():

        def inputBasics():
                print('''
                Inputs are foundational structure in any programming language.
                They allow the user to provide data into a program.\n
                BUILDING A USER INPUT\n
                To build a user input an INPUT VARIABLE must be declared. Like this:
                input("")\n
                1 one_or_two = (input("For selection 1 input 1 for selection 2 input 2: "))
                Always leave a null space between the last letter and closing parenthesis to allow user input.
                ''')
        
                PROCEED_TO_MENU_CLASS.proceedToMenu()


        def variableDeclaration():
            
                print('''This is and overview of basic declarations of Python structures.\n
                VARIABLES\n
                To declare a variable use singular verbs or nouns in snake_case.
                dog = ("Rico") or number = 1\n''')
        
                PROCEED_TO_MENU_CLASS.proceedToMenu()
    
        def functionBasics():
    
    
            print ('''FUNCTIONS\n
            Functions are subroutines within programs that do something. A single program may have several functions.
            Name functions after what part of the program they access in camelCase, OR
            Name them a verb for what the function does...\n
            itAddsThings() or main()
            To declare a function... def itAddsThings(): or def main():\n
            1def itAddsThings 2  (2+2)\n''')
        
            PROCEED_CLASS.proceed()
       
            print('''
            INVOKING FUNCTIONS\n
                       
            Once a function is declared, it needs to be invoked in a subsequent line of the program.
            Invoke the function by: itAddsThings()\n
                       
            RULES FOR FUNCTIONS:\n
                       
            Functions must be FULLY DECLARED before calling them.\n
                       
            1 def itAddsThings:(a, b)   
            2  add = (a + b)
            3  return(add)      
            4 itAddsThings()
            \n''')
        
            PROCEED_TO_MENU_CLASS.proceedToMenu()
    
            
        def dataTypes():
            print ('''
            DATA TYPES\n
                       
            INTEGER\n
                       
            Integers are numbers 1, 2, -1, 0 -3
            Integer are declared like
            number = 4
            \n''')
        
            PROCEED_CLASS.proceed()
               
            print('''
            STRINGS\n
                  
            Strings are words, or numbers. If a string is a number, it is the name of the number not the value of the number.
            Any input from a user is automatically converted to a string, unless explicitly converted during the input call.
            Strings are declared such that:\n
                  
            dog =("Rico") OR
            my_number = "3"
            \n''')
        
            PROCEED_CLASS.proceed()
    
            print('''
                FLOATS\n
                  
                Floats are decimals such as 7.2, 8.1, -.4\n
                  
                Anytime division is done '/' it returns a float.
                Floats are declared the same as integers.\n
                  
                ''')
        
            PROCEED_CLASS.proceed()
    
            print('''
                DICTIONARIES DICT\n
                   
                Dictionaries consist of two constructs, KEYS and VALUES
                KEYS are the UNIQUE IDENTIFIER, or a searchable keyword to access the dictionary.
                VALUES are attributes or properties of the key.
                in other words if it was like an actual dictionary he KEY is the Word, the VALUE is the definition.\n
                   
                DECLARING A DICTIONARY\n
                   
                Dictionaries are declared like:\n
                   
                marine = {}\n # example of empty dictionary
                   
                This is an example of an EMPTY DICTIONARY.\n
                   
                The following 4 outputs are pulling VALUES from the KEY unsc_marine using .get
                VALUES of unsc_marine include name, rank, weapon, and ship.
                \n''')
        
                #Example of populated dictionary
            unsc_marine = {
                "name" : "Johnson",
                "rank" : "Sergeant",
                "weapon" : "MA5B",
                "ship" : "Pillar of Autumn"
                }
            print('The below output is from the program running\n')
    
            print(unsc_marine.get('rank'))
            print(unsc_marine.get('name'))
            print(unsc_marine.get('weapon'))
            print(unsc_marine.get("ship"))
    
            PROCEED_CLASS.proceed()
        
            print('''
            TUPLE\n
                  
            TUPLE is similar to list except TUPLE is immutable, or it cannot be altered once declared.
            TUPLES are used for packing information to and from args. Tuples always have ','
            To declare a TUPLE...  
            \n''')
            
            print('''
                Example of empty TUPLE\n
                snake_stuff = ()\n
                TUPLE populated
                snake_stuff = ("nm7267719","bandana")
                The below output is the program running\n''')
        
                #populated tuple
            snake_stuff = ("nm7267719","bandana")
            print (snake_stuff)
    
            PROCEED_TO_MENU_CLASS.proceedToMenu()
            
        def runBasicsMenu():
                while True:
                    basics_menu =('''
                    MENU -Basics
                    ........................................................................
                    1: Declaring Variables
                    2: Functions Basics
                    3: Data Types             
                    OR ANY OTHER NUMBER TO EXIT.
                    .........................................................................
                    \n''')
                    print(basics_menu)        

                    basic_selection = int(input('Select a Topic\n'))
    
                    if basic_selection == 1:
                        ATOPIC_Y_EXIT.atopic()
                        #print(atopic)
                    #inputBasics()
                    elif basic_selection == 2:
                        ATOPIC_Y_EXIT.atopic()
                        functionBasics()
                    elif basic_selection == 3:
                        ATOPIC_Y_EXIT.atopic()
                        dataTypes()
                    else:
                        ATOPIC_Y_EXIT.exiting()
                        return
        

   
    
    