from navigation import ATOPIC_Y_EXIT, PROCEED_CLASS, PROCEED_TO_MENU_CLASS

# TODO add While/Else structure
# TODO add example of decrementing to 0 with integer for falsey sentinel value
 # while_loops.py contains methods that teach while loop fundamentals.       
class WHILE_LOOP_MENU():

    @staticmethod
    def indefiniteLoopsBasics():
        print('''
        WHILE LOOPS\n
        WHILE loops are useful structures. They have a combo of a few components:\n
        1. Sentinel Value: A value that ends the loop.
        2. Flag: A bool that determines if an event has happened, I also call these switches.
        3. Counter: A structure that keeps counts of iterations, until it reaches the sentinel
           Counters are incremented with += or decremented with -=. 
        4. Loop Body: the part of the loop that does the work
        5. Graceful exit: A way to exit the loop without breaking the program.\n
        The first example will be a an indefinite loop that relies of a sentinel value to exit\n
        sentinel_value = 4
        iteration_counter 0
        while sentinel_value > iteration_counter:
            print("Prints 4 times, because iterations in Python start with 0)
            iteration_counter += iteration counter
        print("Loop exited)\n
        Proceed to run code!\n''')
    
        PROCEED_CLASS.proceed()
    
        # sentinel value exited indefinite loop. 
        sentinel_value = 4 # declare sentinel value
        iteration_counter = 0 # declare counter
        while sentinel_value > iteration_counter:
            print('This will print 4 times.')
            iteration_counter += 1 # increment counter at end of loop workflow
        print('Loop exited.\n') # stick the landing.

        PROCEED_TO_MENU_CLASS.proceedToMenu()

    @staticmethod
    def flagILoop():
    
        print('''The next while loop structure is what I call a flag loop.\n
        A flag loop uses a bool as a sentinel such that:
        counter = 0
        sentinel = False
        while sentinel == False:
            print(counter)
            counter += 1
            if counter == 10:
                sentinel = True:
            else:
                sentinel = False
            print("Loop Exited")\n
        Proceed to run the code.''')
    
        PROCEED_CLASS.proceed()
    
        counter = 0 # set counter
        sentinel = False # set flag, True or False depending on the usecase.
        while sentinel == False:
            print(counter)
            counter += 1 # counter set to increment with each iteration.
            if counter == 10: # when counter hits the prescribed value, sentinel evaluates as True.
                sentinel = True
            else:
                sentinel = False # serves as a redundant switch
            print('Loop Exited.')

        PROCEED_TO_MENU_CLASS.proceedToMenu()

    @staticmethod
    def runWhileLoopMenu():

        while True:
        
            # declarations for indefiniteLoops() menu
            indefinite_loop_menu =('''
            MENU - While Loops
            ........................................................................
            1: While Loop Basics
            2: Flag Controlled While Loops            
            OR ANY OTHER NUMBER TO EXIT.
            .........................................................................
            \n''')
        
            print(indefinite_loop_menu)
            indefinite_loop_selection = int(input('Select a Topic \n'))

            if indefinite_loop_selection == 1:
                ATOPIC_Y_EXIT.atopic()
                WHILE_LOOP_MENU.indefiniteLoopsBasics()
            elif indefinite_loop_selection == 2:
                ATOPIC_Y_EXIT.atopic
                WHILE_LOOP_MENU.flagILoop()
            # TODO add While/Else structure
            # TODO add example of decrementing to 0 with integer for falsey sentinel value    
            else:
                ATOPIC_Y_EXIT.exiting()
                return     
