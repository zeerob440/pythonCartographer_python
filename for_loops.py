from navigation import ATOPIC_Y_EXIT, PROCEED_CLASS, PROCEED_TO_MENU_CLASS

# for_loops.py contains methods for learning for loops. 

class FOR_LOOPS_MENU():
    
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

        proceed()

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
        
        proceed()
        for i in range(3):
                print(i)
        print(i)
    
        proceedToMenu()
    
    def rangeControl():
    #Create simple "for i in range of" FOR LOOP
        
        proceed()
    
        print('''FOR LOOP RANGE CONTROL\n
            In this example you will see...\n
            0
            1
            2\n
            That is because all iterations start with 0 by default in Python. Unless specified otherwise\n
            Proceed to run the code.''')
        
        proceed()

        print("The following is a hardcoded simple FOR LOOP that prints number of iterations.\n")
        for i in range (3):
            print (i)


        proceed()
    
        print('''
            RANGE CONTROL EXAMPLE/n
            To control range in a for loop, it can be declared as\n
            for i in range (1, 4):
                print(i)\n
            print("The RANGE CONTROL the above example starts at 1, and ALWAYS END AT THE HIGHEST DECLARED NUMBER - 1.\n")
            Proceed to run this example!''')
        
        proceed()

        for i in range (1,4):
            print(i)
        print("The RANGE CONTROL the above example starts at 1, and ALWAYS END AT THE HIGHEST DECLARED NUMBER - 1.\n")

        proceedToMenu()

    while True:
        
        # declarations for forLoops() menu
        for_loop_menu =('''
        MENU - For Loops
        ........................................................................
        1: For Loop Basics
        2: Range Control            
        OR ANY OTHER NUMBER TO EXIT.
        .........................................................................
        \n''')