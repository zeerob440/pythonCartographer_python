from navigation import ATOPIC_Y_EXIT, PROCEED_CLASS, PROCEED_TO_MENU_CLASS

'''
selections.py provides training methods for using selections in Python.
'''

class SELECTION_MENU(): 

    @staticmethod
    def selectionBasics():
        print ('''
            SELECTIONS\n
            Selections are an integral software structure used in almost all programs.
            It is one of the methods used to conduct programming logic.\n
            Selections include:
            IF, ELSE SELECTIONS\n
            IF, ELIF, ELSE SELECTIONS\n
            IF IF IF ... SELECTIONS.\n
        ''')

        PROCEED_TO_MENU_CLASS.proceedToMenu()

    @staticmethod
    def ifElseSelections():

        print('''
            IF, ELSE SELECTIONS\n
            IF, ELSE SELECTIONS, create a condition test that executes once branch of the selection if true.
            It executes the opposite branch if the condition is not true.
            IT IS IMPORTANT THAT ELSE DOES NOT REQUIRE A CONDITION\n
            IF, ELSE SELECTION EXAMPLE\n
            1 branch_a_b = (input("Input a for branch a OR any other key for branch b: "))
            2 if branch_a_b == "a":
            3    print("You have selected branch a.")
            4 else: print ("You have selected branch b.")\n
            Hit proceed to try the above example.\n''')
        
        PROCEED_CLASS.proceed()
   
        branch_a_b = (input("Input a for branch a OR any other key for branch b: "))
            # if-else example.
        if branch_a_b == "a":
                print ("You have selected branch a.\n")
        else: print ("You have selected branch b.\n")
   
        print ('The if else selection will print which selection was chosen by the user.\n')

        PROCEED_TO_MENU_CLASS.proceedToMenu()

    @staticmethod
    def ifIfIfSelections():
        print('''
            IF IF IF... SELECTIONS\n
            IF IF IF ...SELECTIONS will search the entire structure and return ALL THE TRUE STATEMENTS.
            IF IF IF...SELECTIONS are useful for finding things.
            in the below example we find an IF IF IF... SELECTION\n
          
            quantity = int(input("Select a number between 1-3: "))
            if quantity >= 1:
                print ("Quantity is greater than or equal to 1. ")
            if quantity >= 2:
                print ("Quantity is greater than or equal to 2. ")
            if quantity >= 3:
                print ("Quantity is greater than or equal to 3. ")  
            \n''')
    
        PROCEED_CLASS.proceed()

        print('The above structure will print all True conditions and not print any False Conditions. Try it.\n')
    
        # if if if example.
        quantity = int(input("Select a number between 1-3: \n"))
        if quantity >= 1:
            print ("Quantity is greater than or equal to 1.\n")
        if quantity >= 2:
            print ("Quantity is greater than or equal to 2.\n")
        if quantity >= 3:
                print ("Quantity is greater than or equal to 3.\n")

        print('''
            If 1 is selected only "Quantity is greater than or equal to 1." will return.\n
            if 2 is selected "Quantity is greater than or equal to 1.", and "Quantity is greater than or equal to 2." will return\n
            if 3 is selected all three statements will return.
            \n''')
        
        PROCEED_TO_MENU_CLASS.proceedToMenu()

    @staticmethod
    def ifElifElifElseSelections():
   
        print ('''
            IF ELIF ELIF ELSE SELECTIONS\n
            In an IF ELIF ELSE Selection...
            Python will search the entire structure for tho only true condition test return the true value.
            In these selections as many ELIF statements as needed can be written as needed.
            If the value is not found in any ELIF structures, it will execute the else branch.\n
            ''')
        
        print('Proceed to try the Mass Effect example.\n')
    

        # if elif else ... example.
        legion_says = int(input("Enter a number between 1-3: "))
        if legion_says <= 1:
            print ("Heretics say 1 is less than 2.\n")
        elif legion_says <=2:
            print ("Heretics say 2 is greater than 1.\n")
        elif legion_says == 3:
            print ("Geth say 3 is greater than 1 and 2.\n")
        else:
            print("You do not follow directions Shepard Commander, you must be indoctrinated.\n")

        print ('''
            In this example, if you picked 1 the program would have returned\n
            Heretics say 1 is less than 2\n
           
            If you picked 2\n
   
            Heretics say 2 is greater than 1\n
           
            If 3 was chosen, it would have printed Legion's line from Mass Effect 2\n
           
            If anything other than 1,2, or 3 was chosen the program would have admonished you for not following directions,
            by executing the else branch.\n
            ''')
    
        PROCEED_CLASS.proceed()      


        print ('''
            IF ELIF ELSE SELECTIONS EXAMPLE 2\n
            IF ELIF ELSE SELECTIONS are a structure that will ONLY EXECUTE THE FIRST CONDITION THAT IS TRUE.\n
            If greater than 3 conditions are needed to complete this sort of structure, ONLY ADDITIONAL ELIF Conditions are created.
            Next we'll explore a IF ELIF ELSE SELECTION using the Sorting Hat from Harry Potter.\n
            ''')
        
        print('Proceed to see how the Sorting Hat might judge you, no pressure.')

        PROCEED_CLASS.proceed()
    
        # if elif else example
        sorting_hat_selection = (input("What virtue do you value most? bravery, intelligence, or friendship: \n"))
        if sorting_hat_selection == ("bravery"):
            print ("You are in House Gryffindor\n")
        elif sorting_hat_selection == ("intelligence"):
            print ("You are in House Ravenclaw.\n")
        elif sorting_hat_selection == "friendship":
            print ("You are in House Hufflepuff.\n")
        else: print ("You are in House Slytherin.\n")

        PROCEED_CLASS.proceed()

        print ('''
        Since this is an IF ELIF... ELSE structure it will only return the true statement.
        IF "bravery was selected, the user is Gryffindor; intelligence Ravenclaw
        friendship Hufflepuff.And if you don't follow rules, the else statement captures
        all other values, Slytherin.\n
        ''')
    
        PROCEED_TO_MENU_CLASS.proceedToMenu()

    @staticmethod
    # renders selections navigation menu for user. 
    def runSelectionsMenu():
        while True:
        
            # declarations for selections() menu
            selections_menu =('''
            MENU - Selections
            ........................................................................
            1: Selection Basics
            2: If Else Selections
            3: If, If, If... Selections
            4: If ELif Else Selections            
            OR ANY OTHER NUMBER TO EXIT.
            .........................................................................
            \n''')
        
            print(selections_menu)
            selection_selection = int(input('Select a Topic \n'))

            if selection_selection == 1:
                ATOPIC_Y_EXIT.atopic
                SELECTION_MENU.selectionBasics()
            elif selection_selection == 2:
                ATOPIC_Y_EXIT.atopic
                SELECTION_MENU.ifElseSelections()
            elif selection_selection == 3:
                ATOPIC_Y_EXIT.atopic
                SELECTION_MENU.ifIfIfSelections()
            elif selection_selection == 4:
                ATOPIC_Y_EXIT.atopic
                SELECTION_MENU.ifElifElifElseSelections()
            else:
                ATOPIC_Y_EXIT.exiting
                return