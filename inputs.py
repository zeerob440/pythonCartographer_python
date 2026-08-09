from navigation import ATOPIC_Y_EXIT, PROCEED_CLASS, PROCEED_TO_MENU_CLASS

# inputs() contains daughter functions inputBasics(), inputTranslation().
class INPUTS_MENU():
   
        @staticmethod
        def inputBasics():

            print('''
            Inputs are foundational structure in any programming language.
            They allow the user to provide data into a program.\n

            REMEMBER ALL INPUTS ARE INITIALLY STRINGS\n

            BUILDING A USER INPUT\n
            To build a user input an INPUT VARIABLE must be declared. Like this:
            user_input = input("")\n
            1 one_or_two = (input("For selection 1 input 1 for selection 2 input 2: "))
            Always leave a null space between the last letter and closing parenthesis to allow user input.
            ''')

        PROCEED_TO_MENU_CLASS.proceedToMenu

        @staticmethod
        def inputTranslation():

            print('''
            INPUT TRANSLATION\n
            Sometimes a certain data type must be used for an INPUT VARIABLE.\n

            Datatype shorthand
            ==============================================================================================
            int is integer: int(input())
            float is a decimal: float(input())
            string is string: all user inputs are string by default, but string(5) is how to translate it.
            bool is boolean: bool(input())
            ===============================================================================================\n
                
            An INPUT VARIABLE with a forced data type is written as:\n
          
            1 my_thing = datatype(input("input message here: "))
            Therefore a variable needing an integer datatype is:
            1 my_number = int(input("pick a number :"))\n
          
            Example...
            This variable has been created a float INPUT VARIABLE.\n
              
            my_number = float(input('Input a number:
            Proceed to use this example.
            ''')
    
            PROCEED_CLASS.proceed()

            print('The below output is from the actual program.\n')

            my_number = float(input("Input a number: "))
            print ("This has prompted the user to input a number, my_number is converted to a float.\n")
            print (my_number)
            print ("As a result it outputs a decimal number.\n")
    
            PROCEED_TO_MENU_CLASS.proceedToMenu()

        @staticmethod
        def runInputsMenu():

            while True:
        
                # declarations for inputs() menu
                inputs_menu =('''
                MENU -Inputs
                ........................................................................
                1: Input Basics
                2: Input Translation            
                OR ANY OTHER NUMBER TO EXIT.
                .........................................................................
                \n''')
        
                print(inputs_menu)
                input_selection = int(input('Select a Topic \n'))

                if input_selection == 1:
                    ATOPIC_Y_EXIT.atopic
                    INPUTS_MENU.inputBasics()
                elif input_selection == 2:
                    ATOPIC_Y_EXIT.atopic()
                    INPUTS_MENU.inputTranslation()
                else:
                    ATOPIC_Y_EXIT.exiting()
                    return
                    # return to navigation.py