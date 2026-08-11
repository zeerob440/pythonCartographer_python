from navigation import ATOPIC_Y_EXIT, PROCEED_CLASS, PROCEED_TO_MENU_CLASS

#input validation.py provides methods for demonstrating and learning input validation.

class INPUT_VALIDATION_MENU(): 

    @staticmethod
    def iValidationBasics():

        print ('''
        Input validation is the process of forcing user input to adhear to specific data types. 
        It is similar to the feeding ramp between the magazine of a firearm and the chamber. 
        Input validation forces intent into the correct position, thereby allowing the
        program to execute as designed.\n
        
        Sometimes input can be validated without TEEF structures or data forcing. Useful methods
        for input validation without these structures include:\n

        isalpha()- checks if input is all chars.
        isdigit()- checks if input is all digits.
        isalnum()- checks if input is is chars or digits without whitespace or spc chars.\n

        These three string methods return a bool if the criteria is met or not met. Which is useful for
        some input validation.\n 
        ''')

        PROCEED_TO_MENU_CLASS.proceedToMenu()

    @staticmethod
    def tryExcept():

        print('''   
        TRY EXCEPT\n 
        TRY EXCEPT are usually contained in a WHILE lOOP. This structure indefinitely prompts the user to input info until
        the correct data type is used.\n
        ''')
    
        PROCEED_CLASS.proceed()

        print (''' EXAMPLE\n
        In the below example the user is prompted to enter an integer.
        The TRY/EXCEPT structure is nested within a WHILE LOOP.
        If the user does not enter an integer, the EXCEPT BRANCH continues the loop.
        In order for the EXCEPT BRANCH to work, THE ERROR THAT WILL OCCUR MUST BE DEFINED.
        Instead of crashing at ValueError, it simply continues the loop when ValueError is returned
        by the EXCEPT BRANCH.\n
        In other words, the EXCEPT BRANCH directs instead of crashing continuing the loop
        If the user enters an integer the TRY BRANCH executes, and the loop breaks with the BREAK command.\n
               
        DO NOT ENTER AN INTEGER on the first try when experimenting with the TRY EXCEPT structure.\n
        
         while True:
            try:
                user_integer = int(input("Enter an integer: "))
                print(f'You enter entered {user_integer}.')
                break
            except ValueError:
                print ("Invalid input, please enter an integer."\n)
              
        Now proceed to try it\n''')

        PROCEED_CLASS.proceed()
    
        # Try Except example.
        while True:
            try:
                user_integer = int(input("Enter an integer: "))
                print(f'You enter entered {user_integer}. Now exiting TE Block.\n')
                break
            except ValueError:
                print ("Invalid input, please enter an integer.\n")

        PROCEED_TO_MENU_CLASS.proceedToMenu()

    @staticmethod
    def tryExceptElseFinally():

        print ('''
        TRY EXCEPT ElSE FINALLY Structures\n
        TEEF structures work such that:\n

        Try block attempts to run the code. 
        IF at any point within the TRY BLOCK the Code fails to run.
        EXCEPT Branch executes.
        IF TRY BRANCH EXECUTES ELSE BRANCH WILL ALSO EXECUTE.
        Finally blocks always execute.\n

        ''')
    
        PROCEED_CLASS.proceed()
    
        # Try Except Else Finally Structure
        print ('''
        Try this TRY EXCEPT ELSE FINALLY Structure.\n
        try:
            if x != 'a':
                # raise immediately exit try block.
                raise ValueError
        except ValueError:
                print('except block executing.')
                print('x does not equal "a"')
        else:
            print('else block executing.')
            print('x deffo equals "a"')
        finally:
            print('finally block executing.')
            print('Finally blocks always execute.')
        \n''')

        print('With 2 attempts, execute each pathway of the TEEF structure.\n')

        PROCEED_CLASS.proceed()

        for attempt in range(2):

            x = input('Enter "a" to execute TEF Blocks, else enter another value to execute EF blocks:\n')

            def teefFunction(x):
                try:
                    if x != 'a':
                        # raise always immediately exits try blocks.
                        raise ValueError
                except ValueError:
                    print('except block executing.')
                    print('x does not equal "a"\n')
                else:
                    print('else block executing.')
                    print('x deffo equals "a"\n')
                finally:
                    print('finally block executing.')
                    print('Finally blocks always execute.\n')

            teefFunction(x)

        print('''
        This concludes the demonstration of a basic TEEF structure.\n
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