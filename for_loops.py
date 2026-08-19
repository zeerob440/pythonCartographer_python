from navigation import ATOPIC_Y_EXIT, PROCEED_CLASS, PROCEED_TO_MENU_CLASS, MENU_INPUT_HANDLER_CLASS

# for_loops.py contains methods for learning for loops. 

class FOR_LOOPS_MENU():

    @staticmethod
    def forLoopBasics():
        print('''
        FOR LOOPS\n
        FOR LOOPS are a type of indefinite loop. They are used to do various tasks such as populating LISTS,
        and completing a task in a set amount of iterations. Iterations are the number of 'laps' ran around the loop.
        FOR LOOPS require a PRIMING VALUE,and a Counter(INCREMENTOR OR DECREMENTOR)
        FOR LOOPS are often described as "for i in range of.." in classroom settings.\n
              
        To set the range on a for loop set as:\n
              
        for i in range(number goes here)
        ''')

        PROCEED_CLASS.proceed()

        print('''LOOP VARIABLES\n
            loop variables are unusual compared to other var declarations. In the following example:\n
              
            for i in range(3):
                print(i)
            print(i)\n
            
            i is the loop variable, it is declared to iterate through the loop, it can just as easily be named
            "widgets" or "doodads". However, loop variables are intended to be used within the scope of the
            for loop. If it is printed outside the scope of the loop, it outputs its last value from when it was in the loop.\n
            
            The example will output\n
            0
            1
            2 # last iteration of for loop
            2 # print statement outside of the loop's scope\n
            Proceed to run the program.
             ''')
        
        PROCEED_CLASS.proceed()
        for i in range(3):
                print(i)
        print(i)
    
        PROCEED_TO_MENU_CLASS.proceedToMenu()

    @staticmethod
    def rangeControl():
    #Create simple "for i in range of" FOR LOOP
        
        PROCEED_CLASS.proceed()
    
        print('''FOR LOOP RANGE CONTROL\n
            In this example you will see...\n
            0
            1
            2\n
            That is because all iterations start with 0 by default in Python. Unless specified otherwise\n
            Proceed to run the code.''')
        
        PROCEED_CLASS.proceed()

        print('''The following is a hardcoded simple FOR LOOP that prints number of iterations.\n
        
        for i in range(3):
            print(i)
        
        \n''')

        for i in range(3):
            print(i)


        PROCEED_CLASS.proceed()
    
        print('''
            RANGE CONTROL EXAMPLE/n
            To control range in a for loop, it can be declared as\n
            for i in range (1, 4):
                print(i)\n
            print("The RANGE CONTROL the above example starts at 1, and ALWAYS END AT THE HIGHEST DECLARED NUMBER - 1.\n")
            Proceed to run this example!''')
        
        PROCEED_CLASS.proceed()

        for i in range (1,4):
            print(i)
        print("The RANGE CONTROL the above example starts at 1, and ALWAYS END AT THE HIGHEST DECLARED NUMBER - 1.\n")

        PROCEED_TO_MENU_CLASS.proceedToMenu()

    @staticmethod
    def eLoopControl():

        print('''Sometimes loop readability is in itself valuable. Especially if work with
            elements in the iterable is needed later in the program.\n
            When such usecases present it good to name the loop var and iterate through the list:
             hockey_league: list = ['Panthers', 'Blackhawks', 'Habs']
            
                    for team in hockey_league:
                        print(team)
            
                    # later in program find team in the iterable  
                    print(hockey_league[2])
                    print(hockey_league.index('Panthers'))
            
                    # search for a team in the list with 'in' key word
                    if 'Panthers' in hockey_league:
                        print('Vamos Gatos!')
                    else:
                        print('No Gatos here.')

            below you will run this example. 

            \n''')

        PROCEED_CLASS.proceed()

        hockey_league: list = ['Panthers', 'Blackhawks', 'Habs']

        for team in hockey_league:
            print(team)

        # later in program find team in the iterable  
        print(hockey_league[2])
        print(hockey_league.index('Panthers'))

        # search for a team in the list with 'in' key word
        if 'Panthers' in hockey_league:
            print('Vamos Gatos!\n')
        else:
            print('No Gatos here.\n')

    @staticmethod
    def runForLoopMenu():

        while True:
        
            # declarations for forLoops() menu
            for_loop_menu =('''
            MENU - For Loops
            ........................................................................
            1: For Loop Basics
            2: Range Control 
            3: Ephemeral Loop Control Loop          
            OR ANY OTHER NUMBER TO EXIT.
            .........................................................................
            \n''')

            print(for_loop_menu)
            for_loop_selection = MENU_INPUT_HANDLER_CLASS.inputVald('Enter an integer to select a structure: \n')

            if for_loop_selection == 1:
                
                FOR_LOOPS_MENU.forLoopBasics()
            elif for_loop_selection == 2:
                ATOPIC_Y_EXIT.atopic
                FOR_LOOPS_MENU.rangeControl()
            elif for_loop_selection == 3:
                FOR_LOOPS_MENU.eLoopControl()
            else:
                ATOPIC_Y_EXIT.exiting()
                return