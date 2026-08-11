from navigation import ATOPIC_Y_EXIT, PROCEED_CLASS, PROCEED_TO_MENU_CLASS

#input validation.py provides methods for demonstrating and learning input validation.

class INPUT_VALIDATION_MENU(): 

    @staticmethod
    def iValidationBasics():

        print ('''
        Input validation is the process of forcing user input to adhear to specific data types. It is similar to the feeding ramp
        between the magazine of a firearm and the chamber. Input validation forces intent into the correct position, thereby allowing the
        program to execute as designed.\n''')

        PROCEED_TO_MENU_CLASS.proceedToMenu()

    @staticmethod
    def tryExcept():

        print('''   
        TRY EXCEPT\n 
        TRY EXCEPT are usually contained in a WHILE lOOP. This structure indefinitely prompts the user to input info until
        the correct data type is used.
        EXAMPLE\n
        ''')
    
        PROCEED_CLASS.proceed()

        print ('''
        In the below example the user is prompted to enter an integer.
        The TRY EXCEPT structure is nested within a WHILE LOOP.
        If the user does not enter an integer, the EXCEPT BRANCH continues the loop.
        In order for the EXCEPT BRANCH to work, THE ERROR THAT WILL OCCUR MUST BE DEFINED, such that instead of crashing at ValueError,
        it simply continues the loop when ValueError is returned by the EXCEPT BRANCH.\n
        In other words, the EXCEPT BRANCH directs instead of crashing continuing the loop
        If the user enters an integer the TRY BRANCH executes, and the loop breaks with the BREAK command.\n
               
        DO NOT ENTER AN INTEGER on the first try when experimenting with the TRY EXCEPT structure.\n
        
         while True:
            try:
                user_integer = int(input("Enter an integer: "))
                print(f'You enter entered {user_integer}.')
                break
            except ValueError:
                print ("Invalid input, please enter an integer.\n")
              
        Now proceed to try it\n''')

        PROCEED_CLASS.proceed()
    
        # Try Except example.
        while True:
            try:
                user_integer = int(input("Enter an integer: "))
                print(f'You enter entered {user_integer}.\n')
                break
            except ValueError:
                print ("Invalid input, please enter an integer.\n")

        PROCEED_TO_MENU_CLASS.proceedToMenu()

    @staticmethod
    def tryExceptElseFinally():

        print ('''
        TRY EXCEPT ElSE FINALLY Structures\n
        In these sort of structures:
        Try is try this operation that may include an error, such as entering a string into an integer input.
        Except must be a defined error such as ValueError, It instructs the program what to do when the error is triggered
        INSTEAD OF CRASHING.\n
        Else in this case only runs if the try attempt succeeds, it is an optional branch.
        Otherwise, one can just run a print command with the try branch.\n
        Finally run no matter what happens, it is also an optional branch.
        IF EXCEPT ELSE FINALLY Structure Example.\n
        Now Try it!\n''')
    
        PROCEED_CLASS.proceed()
    
        # Try Except Else Finally Structure
        print ('''
        Try this TRY EXCEPT ELSE FINALLY Structure.\n
        Enter a string first. Proceed to try and except!\n
        ''')
        PROCEED_CLASS.proceed()

        while True:
            try: 
                integer_two = int(input("Enter another integer: "))
                print (f'You entered {integer_two}.')
            except ValueError:
                print("You did not enter an integer.")
            else: 
                print ("The else branch says, you have entered an integer.ELSE is optional. If structure is nested in WHILE Loop, break loop here.\n")
                break
            finally: print('''The finally branch doesn't care what the user does, it will always print. EVEN IF A LOOP BREAKS BEFOREHAND.\n
                       This originates from the finally structure.\n''')
            
        PROCEED_CLASS.proceed()
    
        print('''
        This structure enters a WHILE LOOP until a integer is entered. If an integer is entered the try, else, and finally branches activate.
        If a non-integer value is entered the loop will execute the EXCEPT branch and reprompt the user\n
        ''')
    
        PROCEED_TO_MENU_CLASS.proceedToMenu()

    @staticmethod
    def runInputValidationMenu():
    
        while True:
        
            # declarations for inputValidation() menu
            validation_menu =('''
            MENU - Input Validation
            ........................................................................
            1: Input Validation Basics
            2: Try Except
            3: Try Except Else Finally            
            OR ANY OTHER NUMBER TO EXIT.
            .........................................................................
            \n''')
        
            print(validation_menu)
            validation_selection = int(input('Select a Topic \n'))

            if validation_selection == 1:
                ATOPIC_Y_EXIT.atopic
                INPUT_VALIDATION_MENU.iValidationBasics()
            elif validation_selection == 2:
                ATOPIC_Y_EXIT.atopic
                INPUT_VALIDATION_MENU.tryExcept()
            elif validation_selection == 3:
                ATOPIC_Y_EXIT.atopic
                INPUT_VALIDATION_MENU.tryExceptElseFinally()
            else:
                ATOPIC_Y_EXIT.exiting()
                return