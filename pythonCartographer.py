'''pythonCartographer is a program that I wrote to help me "map" Python's structures and basic functions.
   
   Version: Charley 01 JAN 2026; pythonCartographer Charley was created to aid navigation of pythonCartographer when it became to large to
   navigate via brute force. It is less butalistic tool, and more application now. Each topic now has while loop controlled submenus invoked from the main menu while loop.
   
   Proudly engineered by Zachary Roberts 11 August, 2025 
   "We should now have access to the main facility. Let’s find the map room."-Cortana'''

print ("This program helps navigate notes and simple structures in the Python language. Zachary Roberts 11 AUG 2025.\n")

# Start

def proceed(): # It asks the user to continue after each example within a lesson.
    any_key_to_continue = input('''\n
                        Press any key to proceed.\n''')

def proceedToMenu():
    any_key_to_menu = input('''\n
                    This concludes this module. Press any key to continue.\n''')
    
# Used to denote that content is being accessed.
atopic = 'Accessing Topic...\n'

#ex used to declare that a menu is exiting.
ex = 'Exiting...\n'

# basics() function, contains daughter functions variableDeclaration(), dataTyped() and functionBasics().
def basics():
    
    def variableDeclaration():
        
        print('''This is and overview of basic declarations of Python structures.\n
            VARIABLES\n
            To declare a variable use singular verbs or nouns in snake_case.
            dog = ("Rico") or number = 1\n''')
    
        proceedToMenu()

    def functionBasics():


        print ('''FUNCTIONS\n
            Functions are subroutines within programs that do something. A single program may have several functions.
            Name functions after what part of the program they access in camelCase, OR
            Name them a verb for what the function does...\n
            itAddsThings() or main()
            To declare a function... def itAddsThings(): or def main():\n
            1def itAddsThings 2  (2+2)\n''')
    
        proceed()
   
        print('''
            INVOKING FUNCTIONS\n
                   
            Once a function is declared, it needs to be invoked in a subsequent line of the program.
            Invoke the function by: itAddsThings()\n
                   
            RULES FOR FUNCTIONS:\n
                   
            Functions must be FULLY DECLARED before calling them.\n
                   
            1 def itAddsThings:()   
            2  (2 + 2)      
            3itAddsThings()
            \n''')
    
        proceedToMenu()

        
    def dataTypes():
        print ('''
        DATA TYPES\n
                   
        INTEGER\n
                   
        Integers are numbers 1, 2, -1, 0 -3
        Integer are declared like
        number = 4
        \n''')
    
        proceed()
           
        print('''
        STRINGS\n
              
        Strings are words, or numbers. If a string is a number, it is the name of the number not the value of the number.
        Any input from a user is automatically converted to a string, unless explicitly converted during the input call.
        Strings are declared such that:\n
              
        dog =("Rico") OR
        my_number = "3"
        \n''')
    
        proceed()

        print('''
        FLOATS\n
              
        Floats are decimals such as 7.2, 8.1, -.4\n
              
        Anytime division is done '/' it returns a float.
        Floats are declared the same as integers.\n
              
        ''')
    
        proceed()

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

        proceed()
    
        print('''
            TUPLE\n
              
            TUPLE is similar to list except TUPLE is immutable, or it cannot be altered once declared.
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

        proceedToMenu()

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
        basic_selection = int(input('Select a Topic \n'))

        if basic_selection == 1:
            print(atopic)
            variableDeclaration()
        elif basic_selection == 2:
            print(atopic)
            functionBasics()
        elif basic_selection == 3:
            print(atopic)
            dataTypes()
        else:
            print(ex)
            break
    
# inputs() contains daughter functions inputBasics(), inputTranslation().
def inputs():
    '''
    inputs() provides overview of input and its daughter functions inputBasics, and inputTranslation.
    it serves as an index of sorts for the daughter functions to be invoked. 
    '''

    def inputBasics():
        print('''
        Inputs are foundational structure in any programming language.
        They allow the user to provide data into a program.\n
        BUILDING A USER INPUT\n
        To build a user input an INPUT VARIABLE must be declared. Like this:
        ("")\n
        1 one_or_two = (input("For selection 1 input 1 for selection 2 input 2: "))
        Always leave a null space between the last letter and closing parenthesis to allow user input.
        ''')

        proceedToMenu()

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
    
        proceed()

        print('The below output is from the actual program.\n')

        my_number = float(input("Input a number: "))
        print ("This has prompted the user to input a number, my_number is converted to a float.\n")
        print (my_number)
        print ("As a result it outputs a decimal number.\n")
    
        proceedToMenu()
    
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
            print(atopic)
            inputBasics()
        elif input_selection == 2:
            print(atopic)
            inputTranslation()
        else:
            print(ex)
            break

# selection() contains daughter functions selectionBasics(), ifElseSelections(), ifIfIFSelections(), and if ElifElifElseSelections()    
def selection(): 

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

        proceedToMenu()
    
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
            Hit proceed to try the above example.''')
        
        proceed()
   
        branch_a_b = (input("Input a for branch a OR any other key for branch b: "))
            # if-else example.
        if branch_a_b == "a":
                print ("You have selected branch a.\n")
        else: print ("You have selected branch b.\n")
   
        print ('The if else selection will print which selection was chosen by the user.\n')

        proceedToMenu()
    
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
    
        proceed()

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
            ''')
        
        proceedToMenu()

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
    
        proceed()

        print ('''
            IF ELIF ELSE SELECTIONS EXAMPLE 2\n
            IF ELIF ELSE SELECTIONS are a structure that will ONLY EXECUTE THE FIRST CONDITION THAT IS TRUE.\n
            If greater than 3 conditions are needed to complete this sort of structure, ONLY ADDITIONAL ELIF Conditions are created.
            Next we'll explore a IF ELIF ELSE SELECTION using the Sorting Hat from Harry Potter.\n
            ''')
        
        print('Proceed to see how the Sorting Hat might judge you, no pressure.')

        proceed()
    
        # if elif else example
        sorting_hat_selection = (input("What virtue do you value most? bravery, intelligence, or friendship: \n"))
        if sorting_hat_selection == ("bravery"):
            print ("You are in House Gryffindor\n")
        elif sorting_hat_selection == ("intelligence"):
            print ("You are in House Ravenclaw.\n")
        elif sorting_hat_selection == "friendship":
            print ("You are in House Hufflepuff.\n")
        else: print ("You are in House Slytherin.\n")

        proceed()

        print ('''
        Since this is an IF ELIF... ELSE structure it will only return the true statement.
        IF "bravery was selected, the user is Gryffindor; intelligence Ravenclaw
        friendship Hufflepuff.And if you don't follow rules, the else statement captures
        all other values, Slytherin.\n
        ''')
    
        proceedToMenu()
    
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
            print(atopic)
            selectionBasics()
        elif selection_selection == 2:
            print(atopic)
            ifElseSelections()
        elif selection_selection == 3:
            print(atopic)
            ifIfIfSelections()
        elif selection_selection == 4:
            print(atopic)
            ifElifElifElseSelections()
        else:
            print(ex)
            break

# inputValidation() contains daughter functions inputValidationBasics(), tryExcept(), and tryExceptElseFinally()
def inputValidation(): 

    def iValidationBasics():

        print ('''
        Input validation is the process of forcing user input to adhear to specific data types. It is similar to the feeding ramp
        between the magazine of a firearm and the chamber. Input validation forces intent into the correct position, thereby allowing the
        program to execute as designed.\n''')

        proceedToMenu()

    def tryExcept():

        print('''   
        TRY EXCEPT\n 
        TRY EXCEPT are usually contained in a WHILE lOOP. This structure indefinitely prompts the user to input info until
        the correct data type is used.
        EXAMPLE\n
        ''')
    
        proceed()

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

        proceed()
    
        # Try Except example.
        while True:
            try:
                user_integer = int(input("Enter an integer: "))
                print(f'You enter entered {user_integer}.\n')
                break
            except ValueError:
                print ("Invalid input, please enter an integer.\n")

        proceedToMenu()
    
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
    
        proceed()
    
        # Try Except Else Finally Structure
        print ('''
        Try this TRY EXCEPT ELSE FINALLY Structure.\n
        Enter a string first. Proceed to try and except!\n
        ''')
        proceed()

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
            
        proceed()
    
        print('''
        This structure enters a WHILE LOOP until a integer is entered. If an integer is entered the try, else, and finally branches activate.
        If a non-integer value is entered the loop will execute the EXCEPT branch and reprompt the user\n
        ''')
    
        proceedToMenu()
    
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
            print(atopic)
            iValidationBasics()
        elif validation_selection == 2:
            print(atopic)
            tryExcept()
        elif validation_selection == 3:
            print(atopic)
            tryExceptElseFinally()
        else:
            print(ex)
            break

# forLoops() contains daughter functions forLoopsBasics(), and RangeControl().
def forLoops():

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
        
        print(for_loop_menu)
        for_loop_selection = int(input('Select a Topic \n'))

        if for_loop_selection == 1:
            print(atopic)
            forLoopBasics()
        elif for_loop_selection == 2:
            print(atopic)
            rangeControl()
        else:
            print(ex)
            break    

# indefiniteLoops() contains daughter functions indefiniteLoopsBasics, and flagILoops().       
def indefiniteLoops():

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
    
        proceed()
    
        # sentinel value exited indefinite loop. 
        sentinel_value = 4 # declare sentinel value
        iteration_counter = 0 # declare counter
        while sentinel_value > iteration_counter:
            print('This will print 4 times.')
            iteration_counter += 1 # increment counter at end of loop workflow
        print('Loop exited.\n') # stick the landing.

        proceedToMenu()
    
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
    
        proceed()
    
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

        proceedToMenu()

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
            print(atopic)
            indefiniteLoopsBasics()
        elif indefinite_loop_selection == 2:
            print(atopic)
            flagILoop()
        else:
            print(ex)
            break    

def functions():

    def functionBasics():
        print('''
        FUNCTIONS\n
        When programming in any language it is important to not repeat yourself with repetitive tasks.
        This is know as the "don't repeat yourself" principal. (DRY).
        Functions are essential for completing repetitive tasks. They can be used to call locations in a program,
        such as they are used in pythonCartographer, or to do repetitive math operations.''')

        proceed()      

        print(''' 
        ARGUMENTS\n
        Functions are designed to take arguments like this:\n
        itAddsThings(a, b)\n
        For argument's sake, the arguments d = 5 and f = 15 are globally declared variables.
        The function finds these two arguments and expects to do something with them.
        in this case it will add them.\n
        ''')
    
        proceed()

        print('''
        To build out the function it has to be directed to do something with d and f.\n
        itAddsDF(d, f):
            added = d + f
            return added\n
              
        itAddsDF(d, f) # function invoked with arguments

        d_plus_f = itAddsDF(d, f) #declared var to store return value in

        print (d_plus_f) # output return value
        
        # it will return 20
       
        sum = d + f takes the targeted global arguments, adds them, and stores the value in sum. 
        Once that happens return is used to make sum accessible to the main program, from here it can be printed, 
        or moved into another structure as needed. Proceed to try it.\n
        ''')
    
        proceed()


        d = 5 # argument variables are declared 
        f = 15
        def itAddsDF(d, f): # function is declared
            added = d + f
            return added
        
        itAddsDF(d, f) # function invoked with arguments
        d_plus_f = itAddsDF(d, f) #declared var to save return value in
        print (d_plus_f) # output return value

        proceedToMenu()

    # This lesson is longer because it reuses the same code throughout the lesson.   
    def intermediateFunctionOps():

        print('''OUTPUT RETURNS\n
            Producing output for returns follows this process:\n
            1. Declare Vars needed for function arguments
            2. Declare Functions.
            3. Invoke functions.
            4. Save returns to variables in the main program.
            ''')
        
        proceed()
        print('''EXAMPLE CODE OF OUTPUT RETURNS.
             # Example of simple function, doing math ops, outputting function returns. 
        a = 10 # globally declared var
        b = 5  # globally declared var

        # functions below declared with variables as arguments.
        def itAddsThings(a, b): 
            sum = a + b
            return sum 

        def itSubtractsThings(a, b):
            difference = a - b
            return difference

        def itMultipliesThings(a, b):
            product = a * b
            return product

        def itDividesThings(a, b):
            quotient = int(a / b)
            return quotient
        
        #functions invoked with args
        itAddsThings(a, b)
        itSubtractsThings(a, b)
        itMultipliesThings(a, b)
        itDividesThings(a, b)

        #returns saved to variables 
        add = itAddsThings(a, b)
        subtract = itSubtractsThings(a, b)
        multiply = itMultipliesThings(a, b)
        divide = itDividesThings(a, b)

        # variables printed
        print(add)
        print(subtract)
        print(multiply)
        print(divide)\n
        
        Output will be:\n
        
        15
        5
        50
        2\n
        Proceed to run code.
        ''')

        proceed()

        # Example of simple function, doing math ops, outputting function returns. 
        a = 10 # globally declared var
        b = 5  # globally declared var

        # functions below declared with variables as arguments.
        def itAddsThings(a, b): 
            sum = a + b
            return sum 

        def itSubtractsThings(a, b):
            difference = a - b
            return difference

        def itMultipliesThings(a, b):
            product = a * b
            return product

        def itDividesThings(a, b):
            quotient = int(a / b)
            return quotient
        
        #functions invoked with args
        itAddsThings(a, b)
        itSubtractsThings(a, b)
        itMultipliesThings(a, b)
        itDividesThings(a, b)

        #returns saved to variables 
        add = itAddsThings(a, b)
        subtract = itSubtractsThings(a, b)
        multiply = itMultipliesThings(a, b)
        divide = itDividesThings(a, b)

        # variables printed
        print(add)
        print(subtract)
        print(multiply)
        print(divide)


        proceed()
    
    
        print('''OUTPUT FUNCTION WITH f-STRING\n
        It is possible to print a function to an f-string by:\n
        print(f'a + b = {itAddsThings(a, b)}')\n
        print(f'a - b = {itSubtractsThings(a, b)}')
        print(f'a * b = {itMultipliesThings(a, b)}')\n
        print(f'a / b = {itDividesThings(a, b)}')\n  
        Proceed to see the values output in f-strings.\n
        ''')
    
        proceed()

        # printing functions to f-string is possible.
        print(f'a + b = {itAddsThings(a, b)}\n')
        print(f'a - b = {itSubtractsThings(a, b)}\n')
        print(f'a * b = {itMultipliesThings(a, b)}\n')
        print(f'a / b = {itDividesThings(a, b)}\n')

        proceed()

        print('''
        MAKING NEW VARIABLES WITH FUNCTIONS\n
        It is possible to store a function return in a variable once the value is returned to main.
        It is also possible to add a constants to a function return to alter the value. The
        examples below are how to build these structures.\n
          
        print(itMultipliesThings(a, b) + 9)
        divide_multiply_sum = (itDividesThings(a, b) + itMultipliesThings(a, b))
        print(divide_multiply_sum)\n
        output will be:\n
        52
        59\n
        ''')
    
        print('Proceed to run the above code.\n')

        proceed()

        # function return values can be used to create new variables and print statements.
        print(itMultipliesThings(a, b) + 9)
        divide_multiply_sum = (itDividesThings(a, b) + itMultipliesThings(a, b))
        print(divide_multiply_sum)

        proceed

        print('''
        REUSING FUNCTIONS\n
        One of the advantages of functions is that they can be reused. This can be done by simply changing the args.
        For instance using this code we just ran, we'll add two more values for the itAddsThings function to print.\n
        
        divide_multiply_sum = (itDividesThings(a, b) + itMultipliesThings(a, b))

        add _subtract_sum = (itAddsThings(a,b) + itSubtractsThings(a, b))

        print(add_subtract_sum)     

        print(divide_multiply_sum)

        # using itAddsThings function with new args to add divide_multiply_sum and add_subtract_sum
        itAddsThings(divide_multiply_sum, add_subtract_sum)

        print(itAddsThings(divide_multiply_sum, add_subtract_sum))\n
        It will output\n
        20
        52''')
    
        print('Proceed to run code.\n')

        proceed()

        divide_multiply_sum = (itDividesThings(a, b) + itMultipliesThings(a, b))

        add_subtract_sum = (itAddsThings(a,b) + itSubtractsThings(a, b))

        print(add_subtract_sum)

        print(divide_multiply_sum)

        # using itAddsThings function with new args to add divide_multiply_sum and add_subtract_sum
        itAddsThings(divide_multiply_sum, add_subtract_sum)

        print(f'''
        The new args in itAddsThings(divide_multiply_sum, add_subtract_sum)
        is:{itAddsThings(divide_multiply_sum, add_subtract_sum)}.\n''')

        proceedToMenu()
    while True:
        
        # declarations for functions() menu
        functions_menu =('''
        MENU - Functions
        ........................................................................
        1: Functions Basics
        2: Intermediate Functions Operations           
        OR ANY OTHER NUMBER TO EXIT.
        .........................................................................
        \n''')
        
        print(functions_menu)
        functions_selection = int(input('Select a Topic \n'))

        if functions_selection == 1:
            print(atopic)
            functionBasics()
        elif functions_selection == 2:
            print(atopic)
            intermediateFunctionOps()
        else:
            print(ex)
            break    

def listsPopulation():
    
    def populateLists():
        print('''
        POPULATING LISTS\n
        Lists are a great way to store data. Lists can store virtually any Python data type.
        They can be populated via hardcoding values into them such that:\n
        my_list =['dog', 'cat']
        their_list = [2 ,'cherry','mouse']\n
        In Python data types do not need to be the same to create a list like in many other languages.
        ''')
    
        proceed()

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
    
        proceed()

        dog_list = ['Rico']
        new_dog = input("Enter a new dog: ")
        dog_list.append(new_dog)
        print(dog_list)
    
        proceedToMenu()

    def populateListForLoop():

        print('''
        POPULATING LIST WITH FOR LOOP\n
        Lists are often populated with loops the example below is:\n
          
        user_things = [] # declare empty list.
        for i in range(3):# initiate for loop.
            user_thing_input = input('Enter a anything: ')# declare user input variable.
            user_things.append(user_thing_input)# use .append() method to populate the list
        print(user_things)# print raw list.\n
          
        Proceed to try it. The code will allow you to input 3 items.
        ''')
    
        proceed()

        # Below is an example of populating a list with the .append() method.
        user_things = [] # declare empty list.
        for i in range(3):# initiate for loop.
            user_thing_input = input('Enter anything: ')# declare user input variable.
            user_things.append(user_thing_input)# use .append() method to populate the list
        print(user_things)# print raw list.

        proceedToMenu()

    def populateListInsert():

        print('''POPULATING LIST WITH insert()\n
          Another way to populate a list is with the insert()method.
          insert() is used to populate an item at a specific index, the method need an index argument and a item to insert, such  that:\n
          cat_list = ['tabby', 'siamese', 'persian']\n
          cat_list.insert(1, 'main coon')\n
          print(cat_list)\n
          
          proceed to run this code.\n
          ''')
    
        proceed()

        cat_list = ['tabby', 'siamese', 'persian']
        cat_list.insert(1, 'main coon')
        print (cat_list)

        proceedToMenu()
    
    def populateListWhileLoop():
        print('''
        POPULATING LIST WITH WHILE LOOP\n
        It is also possible to populate a list with an while loop. Below is an example of how this is achieved\n
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

        proceed()

        another_list = [] #declare empty list
        append_list = True
        while append_list:
            list_apendenator = input('Enter an item to list: ')
            another_list.append(list_apendenator)
            sentinel_prompt = input('Would you like to add another item? Enter "y" or "n": ')
            if sentinel_prompt == ('y'):      
                append_list = True
            else: append_list = False
        print('You entered\n')
        print(*another_list)# * is used for argument unpacking it removes commas and brackets.

        proceedToMenu()

    def populateListSplit():
        print('''
        POPULATING LIST WITH .split()\n
        Lists can be created using the .split() method. However, it is important to warn the user
        that this method of input is being used. The .split() method uses space to separate several items in a list
        the list is then created when the user presses enter
        Below is an example of how this method is used for user input.\n
          
        enter_items = input('enter and item separated by space ')# input variable
        items = enter_items.split() create a variable to contain the items once split into a list the var becomes the list.
        print(items) # items is now a list\n.
        Now you try:\n
        ''')
    
        proceed()

        enter_items = input('Enter an item separated by space. ')
        items = enter_items.split()
        print(items)

        proceedToMenu()
    
    def populateListConcat():

        print('''JOINING LISTS WITH CONCATENATION\n
        Another method of populating lists is to concatenate them. Such that you simply add the list together in another variable.
        since you are concatenating two list the new variable is also list such that:\n
         A simple program demonstrating how to concatenate lists.

        list1 = [1, 2 , 3]
        listA = ['a','b','c']\n

        combined_list = (list1 + listA)\n

        print(combined_list)\n

        Proceed to run this program, it will output [1, 2 ,3, 'a', 'b', 'c']
        ''')
    
        proceed()
        list1 = [1, 2 , 3]
        listA = ['a','b','c']

        combined_list = (list1 + listA)

        print(combined_list)

        proceedToMenu()

    while True:
        
        # declarations for populateLists() menu
        populate_list_menu =('''
        MENU - 
        ........................................................................
        1: List Population .append
        2: List Population for loop
        3: List Population insert()
        4: List Population While Loop
        5: List Population split()
        6: List Population Concatenation           
        OR ANY OTHER NUMBER TO EXIT.
        .........................................................................
        \n''')
        
        print(populate_list_menu)
        populate_list_selection = int(input('Select a Topic \n'))

        if populate_list_selection == 1:
            print(atopic)
            populateLists()
        elif populate_list_selection == 2:
            print(atopic)
            populateListForLoop()
        elif populate_list_selection == 3:
            print(atopic)
            populateListInsert()
        elif populate_list_selection == 4:
            print(atopic)
            populateListWhileLoop()
        elif populate_list_selection == 5:
            print(atopic)
            populateListSplit()
        elif populate_list_selection == 6:
            print(atopic)
            populateListConcat()
        else:
            print(ex)
            break        

def depopulatingLists():

    def depopulateListBasics():

        print('''DEPOPULATING LISTS\n
          Modifying lists is a typical workflow in Python, items need to be added, and items need to be removed.
          We will explore how to depopulate lists with the pop() and remove() methods, and typical structures whereby these methods are
          used.\n''')
        
        proceed()
    
        print('''DEPOPULATING LIST WITH pop() and remove()\n
          The pop() method is a technique to remove the LAST ITEM of a list if no argument is added, or it can remove the item
          in a specific index if an argument is added, below is an example of how pop() is used in both manners.
          remove() removes the first occurrence of the value specified in its arg.\n
          
        the_list = ['dog', 'cat', 'bird', 'cat', 'whale', 'cat', 'dolphin']
        the_list.pop() #removes last item of list "dolphin
        print(the_list)
        the_list.pop(2) #removes item in the second index "bird"
        print(the_list)
        the_list.remove('cat') #removes the first "cat" from the list
        print(the_list)\n
          
        Proceed to run the code.\n''')
    
        proceed()
    
        the_list = ['dog', 'cat', 'bird', 'cat', 'whale', 'cat', 'dolphin']
        the_list.pop() #removes last item of list "dolphin
        print(the_list)
        the_list.pop(2) #removes item in the second index "bird"
        print(the_list)
        the_list.remove('cat') #removes the first "cat" from list
        print(the_list)

        proceedToMenu()

    def depopulateListWList():
        print('''REMOVING LIST ITEMS WITH ANOTHER LIST\n
        Items can be removed from one list by another list with remove(). This is done by iterating through one list
        and then searching for duplicate items in another list and removing them.
        like this:\n
        

        list26 = [1, 2, 3, 4, 5, 6]
        list62 = [2, 4, 6]

        for item26 in list26:
            if item26 in list62:
                list26.remove(item26)
        print(*list26)\n
          
        It will output 1 3 5 since * unpacker is used here
    
        Proceed to run the code''')

        proceed()

        # remove items from one list that are in another.

        list26 = [1, 2, 3, 4, 5, 6]
        list62 = [2, 4, 6]

        for item26 in list26:
            if item26 in list62:
                list26.remove(item26)
        print(*list26)

        proceedToMenu()

    def depopulateWListComp():

        print('''REMOVE WITH LIST COMPREHENSION\n
            FIXME: create list comprehension example. ''')

        proceedToMenu()

    while True:
        
        # declarations for depopulateLists() menu
        depopulate_menu =('''
        MENU - Depopulating Lists
        ........................................................................
        1: Depopulate List Basics
        2: Depopulate List with Another List
        3: Depopulate List with List Comprehension           
        OR ANY OTHER NUMBER TO EXIT.
        .........................................................................
        \n''')
        
        print(depopulate_menu)
        depopulate_selection = int(input('Select a Topic \n'))

        if depopulate_selection == 1:
            print(atopic)
            depopulateListBasics()
        elif depopulate_selection == 2:
            print(atopic)
            depopulateListWList()
        elif depopulate_selection == 3:
            print(atopic)
            depopulateWListComp
        else:
            print(ex)
            break 

def dictionaries():
    print("FIX ME: dictionary content goes here")
    # place content and menu for dictionaries here

        
     
def main():# it serves as the main menu of pythonCartographer, one may call it the "index".
        while True:
            menu =('''
            MENU-pythonCartographer
            -----------------------------------------------------------------------
            1: BASICS, VARIABLE DECLARATIONS, DATA TYPES
            2: INPUT
            3: SELECTIONS
            4: INPUT VALIDATION
            5: FOR LOOPS
            6: INDEFINITE LOOPS
            7: FUNCTIONS
            8: POPULATING LISTS
            9: DEPOPULATING LISTS
            10: DICTIONARIES
            OR ANY OTHER NUMBER TO EXIT.
            ------------------------------------------------------------------------
            ''')

            print(menu)

            select_structure = int(input("Input structure you would like to review: "))
            if select_structure == 1:
                print ("Accessing Basics...\n")
                basics()
            elif select_structure == 2:
                print ("Accessing Inputs...\n")
                inputs()
            elif select_structure == 3:
                print ("Accessing Selections...\n")
                selection()
            elif select_structure == 4:
                print ("Accessing Input Validation...\n")
                inputValidation()
            elif select_structure == 5:
                print("Accessing For Loops...\n")
                forLoops()
            elif select_structure == 6:
                print('Accessing indefinite loops...\n')
                indefiniteLoops()
            elif select_structure == 7:
                print('Accessing Functions...\n')
                functions()
            elif select_structure == 8:
                print('Accessing Populating Lists...\n')
                listsPopulation()
            elif select_structure == 9:
                print('Accessing Depopulating Lists\n')
                depopulatingLists()
            elif select_structure == 10:
                print('Accessing Dictionaries\n')
                dictionaries()
            else:
                print('Exiting pythonCartographer!')
                break
            
main()
'''
Daughter functions of main:
basics()
inputs()
inputValidation()
'''     

 

