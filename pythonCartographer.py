'''pythonCartographer is a program that I wrote to help me "map" Python's structures and basic functions.'''
'''Proudly engineered by Zachary Roberts 11 August, 2025. 
    "We should now have access to the main facility. Let’s find the map room."-Cortana'''

print ("This program helps navigate notes and simple structures in the Python language. Zachary Roberts 11 AUG 2025.\n")

# Main menu of program. Prints valid input selection, runs through indefinate loop.     
def main():# it serves as the main menu of Python Cartographer, one may call it the "index"
    print ('''
        Basics, variable declarations, data types that sort: 1
        Input: 2
        IF Else selections, IF IF IF..Else selections IF ELIF ElSE Selections: 3
        Input Validation: 4
        For Loops: 5
        Indefinate Loops: 6
        Functions: 7
        Lists: 8\n''')
    select_structure = int(input("Input structure you would like to review: "))
    if select_structure == 1:
        print ("Accessing Basics...\n")
        basics()
    elif select_structure == 2:
        print ("Accessing Inputs...\n")
        inputs()
    elif select_structure == 3:
        print ("Accessing Selections\n")
        selection()
    elif select_structure == 4:
        print ("Accessing Input Validation...\n")
        inputValidation()
    elif select_structure == 5:
        print("Accessing For Loops...\n")
        for_loops()
    elif select_structure == 6:
        print('Accessing indefinite loops...\n')
        indefiniteLoops()
    elif select_structure == 7:
        print('Accessing Functions...')
        functions()

def returnsToMAin():# It returns user to main menu at the end of a function. 
    return_key = (input("Press any key when ready to return to Main Menu. "))
    while True: 
        main()

def proceed(): # It askes the user to continue after each example within a module
    any_key_to_continue = input('Press any key to advance to the next example:\n')

def basics():# This module provides an overview of the basic structures and data types used in Python.
    print ('''This is and overview of basic declerations of Python structures.\n
           VARIABLES\n
           To declare a variable use singular verbs or nouns in snake_case.
           dog = ("Rico") or number = 1\n''')
    
    proceed()

    print ('''FUNCTIONS\n
           Functions are subroutines within programs that do something. A single program may have several functions.
           Name functions after what part of the program they access in camelCase, OR
           Name them a verb for what the function does...
           itAddsThings() or main()
           To declare a function... def itAddsThings(): or def main():\n
           1def itAddsThings 2  (2+2)\n''')
    
    proceed()
   
    print ('''INVOKING FUNCTIONS\n
           Once a function is declared, it needs to be invoked in a subsequent line of the program.
           Invoke the function by: itAddsThings()\n
           RULES FOR FUNCTIONS:\n
           Fucntions must be FULLY DECLARED before calling them.
           1 def itAddsThings:()\n
           2  (2 + 2)\n
           3itAddsThings()\n''')
    
    proceed()
    
    print ('''DATA TYPES\n
           INTEGER\n
           Integers are numbers 1, 2, -1, 0 -3
           Integer are declared like
           number = 4\n''')
    
    proceed()
           
    print('''STRINGS\n
          Strings are words, or numbers. If a string is a number, it is the name of the number not the value of the number
          Strings are declared such that:
          dog =("Rico") OR
          my_number = "3"\n''')
    
    proceed()

    print ('''FLOATS\n
        Floats are decimals such as 7.2, 8.1, -.4\n
        Anytime division is done '/' it returns a float.
        Floats are declared the same as integers.\n''')
    
    proceed()

    print ('''DICTONARIES DICT\n
           Dictionaries consist of two constructs, KEYS and VALUES
           KEYS are the UNIQUE IDENTIFIER, or a searchable keyword to access the dictionary.
           VALUES are attributes or properties of the key.
           in other words if it was like an actual dictionary he KEY is the Word, the VALUE is the definition.
           DECLARING A DICTIONARY
           Dictionaries are declared like:\n
           marine = {}\n
           This is an example of an EMPTY DICTIONARY.\n
           The following 4 outputs are pulling VALUES from the KEY unsc_marine using .get
           VALUES of unsc_marine include name, rank, weapon, and ship.\n''')
    #Example of populated dictionary
    unsc_marine = {
        "name" : "Johnson",
        "rank" : "Sergeant",
        "weapon" : "MA5B",
        "ship" : "Pillar of Autumn"
        }
    print(unsc_marine.get('rank'))
    print(unsc_marine.get('name'))
    print(unsc_marine.get('weapon'))
    print(unsc_marine.get("ship"))

    proceed()
    
    print('''TUPLE\n
        TUPLE is similar to list except TUPLE is immutable, or it cannot be altered once declared.
        To decalre a TUPLE...''')
    print('''Example of empty TUPLE\n
        snake_stuff = ()\n
        TUPLE populated
        snake_stuff = ("nm7267719","bandana")\n''')
    
    #populated tuple
    snake_stuff = ("nm7267719","bandana")
    print (snake_stuff)

    returnsToMAin()  

def inputs(): # This function provides overview of inputs.

    print ('''Inputs are foundational structure in any programming language.
           They allow the user to provide data into a program.\n
           BUILDING A USER INPUT\n
           To build a user input an INPUT VARIABLE must be declared. Like this:
           ("")\n
           1 one_or_two = (input("For selection 1 input 1 for selection 2 input 2: "))
           Always leave a null space between the last letter and closing parenthesis to allow user input.\n
           INPUT TRANSLATION\n
           Sometimes a certain data type must be used for an INPUT VARIABLE.
           int is integer
           float is a decimal
           string is string
           bool is boolean
           An INPUT VARAIBLE with a forced data type is written as:\n
           1 my_thing = datatype(input("input message here: "))
           Therefore a variable needing an integer datatype is:
           1 my_number = int(input("pick a number :"))\n
           Example...
           This varible has been created a float INPUT VARIABLE.
           my_number = float(input('Input a number: '\n''')

    my_number = float(input("Input a number: "))
    print ("This has prompted the user to input a number, my_number is converted to a float.")
    print (my_number)
    print ("As a result it outputs a decimal number.")
    
    returnsToMAin()  
def selection(): # This function highlights selection basics.
    print ('''SELECTIONS\n
           Selections are an integral software structure used in almost all programs.
           Selections include:
           IF, ELSE SELECTIONS\n
           IF, ELIF, ELSE SELECTIONS\n
           IF,IF,ELSE SELECTIONS\n
           IF IF IF ... SELECTIONS.\n''')

    proceed()

    print('''IF, ELSE SELETIONS\n
        IF, ELSE SELECTIONS, create a condition test that executes once branch of the selection if true.
        It executes the oppisite branch if the condition is not true.
        IT IS IMPORTANT THAT ELSE DOES NOT REQUIRE A CONDITION\n
        IF, ELSE SELECTION EXAMPLE\n
        1 branch_a_b = (input("Input a for branch a OR any other key for branch b: "))
        2 if branch_a_b == "a":
        3    print("You have selected branch a.")
        4 else: print ("You have selected branch b.")\n''')
   
    branch_a_b = (input("Input a for branch a OR any other key for branch b: "))
    # if-else example.
    if branch_a_b == "a":
        print ("You have selected branch a.\n")
    else: print ("You have selected branch b.\n")
   
    print ('The if else selection will print which selction was chosen by the user.\n')

    proceed()
    
    print('''
        IF IF IF... ELSE SELECTIONS\n
        IF IF IF ...ELSE SELECTIONS are evaluated as 3 seperate distinct selections by Python.
        However, in this structure, THE ELSE STATEMENT DOES NOT NEED A CONDITION, IT TRIGGERS WHEN THE PREVIOUS
        IF, AND ONLY IF THE PREVIOUS IF CONDITION TEST IS FALSE.\n
        The IF IF IF ELSE STRUCTURE has a very narrow use case.It is best to think of it as
        2 seperate if selections with no else statement and one if else selection.
        IF IF IF ELSE SELECTION EXAMPLE\n''')
    
    
    # if if...else example.
    quantity = int(input("Select a number between 1-3: \n"))
    if quantity >= 1:
        print ("Quantity is greater than or equal to 1.\n")
    if quantity >= 2:
        print ("Quantity is greater than or eqaul to 2.\n")
    if quantity >= 3:
        print ("Three is greater than 1 and 2.")
    else: print("Quantity is greater than or equal to 3, OR equal to 2, OR less than or equal to 1.\n")

    proceed()
   
    print ('''IF IF ... SELECTIONS\n
           In an IF IF Selection...
           Python will search the entire structure for true condition tests and return all true condition tests.
           Therefore, it will continue to search the structure even after it has found the first true condition test.\n''')
    

    # if if ... example.
    legion_says = int(input("Enter a number between 1-3: "))
    if legion_says <= 1:
        print ("Heretics say 1 is less than 2.\n")
    if legion_says <=2:
        print ("Heretics say 2 is greater than 1.\n")
    if legion_says == 3:
        print ("Geth say 3 is greater than 1 and 2.\n")
    if legion_says >3:
        print("You do not follow directions Shepard Commander, you must be indoctrinated.\n")

    print ('''In this example, if you picked 1 or 2 the program would have returned\n
           1 Heritics say 2 is greater than 1\n2 Heretics say 2 is greater than
           it would have skipped "Geth say 3 is greater than 1 and 2"
           If 3 was chosen, it would have printed Legion's line from Mass Effect 2.
           If > 3 it would have admonished you for not following directions.\n''')
    
    proceed()

    print ('''IF ELIF ELSE SELECTIONS\n
           IF ELIF ELSE SELECTIONS are a structure that will ONLY EXECUTE THE FIRST CONDITION THAT IS TRUE.\n
           If greater than 3 conditions are needed to complete this sort of structure, ONLY ADDITIONAL ELIF Conditions are created.
           Next we'll explore a IF ELIF ELSE SELECTION using the Sorting Hat from Harry Potter.\n''')
    
    # if elif else example
    sorting_hat_selection = (input("What virtue do you value most? bravery, intelligence, or friendship: \n"))
    if sorting_hat_selection == ("bravery"):
        print ("You are in House Gryffindor\n")
    elif sorting_hat_selection == ("intelligence"):
        print ("You are in House Ravenclaw.\n")
    elif sorting_hat_selection == "friendship":
        print ("You are in House Hufflepuff.\n")
    else: print ("Your are in House Slytherin.\n")

    proceed()

    print ('''Since this is an IF ELIF... ELSE structure it will only return the true statement.
           IF "bravery was selected, the user is Gryffindor; intelligence Ravenclaw
           friendship Hufflepuff.And if you don't follow rules, the else statement captures
           all other values, Slytherin.\n
           This concludes the selection module.\n''')

    returnsToMAin()

def inputValidation(): # input validation function.
    print ('''Input validation is the process of forcing user input to adhear to specific data types. It is similar to the feeding ramp
        between the magazine of a firearm and the chamber.Input validation forces intent into the correct postion, thereby allowing the
        program to execute as designed.\n
        TRY EXCEPT SELECTIONS\n 
        TRY EXCEPT SELECTIONS are usually contained in a WHILE lOOP. This structure indefinately prompts the user to input info until
        the correct data type is used.
        EXAMPLE\n''')
    
    proceed()

    print ('''In this example the user is prompted to enter an integer.
           The TRY EXCEPT structure is nested within a WHILE LOOP.
           If the user does not enter a integer, the EXCEPT BRANCH continues the loop.
           In order for the EXCEPT BRANCH to work, THE ERROR THAT WILL OCCUR MUST BE DEFINED, such that instead of crashing at ValueError,
           it simply continues.
           the loop when ValueError is returned by the EXCEPT BRANCH.\n
           In other words, the EXCEPT BRANCH directs instead of chashing continue the loop
           If the user enters an integer the TRY BRANCH executes, and the loop breaks with the BREAK commannd.
           Do not enter an integer first to experiment with the TRY EXCEPT structure.\n''')
    # Try Except example.
    while True:
        try:
            user_integer = int(input("Enter an integer: "))
            print(f'You enter entered {user_integer}.')
            break
        except ValueError:
            print ("Invalid input, please enter an integer.\n")

    proceed()
    
    print ('''TRY EXCEPT ElSE FINALLY Structures\n
           In these sort of structures:
           Try is try this operation that may include an error, such as entering a string into an integer input.
           Except must be a defined error such as ValueError, It instructs the program what to do when the error is trigged
           INSTEAD OF CRASHING.\n
           Else in this case only runs if the try attempt succedes, it is an optional branch.
           Otherwise, one can just run a print command with the try branch.\n
           Finally run no matter what happens, it is also an optional branch.
           IF EXCEPT ELSE FINALLY Structure Example\n''')
    
    proceed()
    
    # Try Except Else Finally Structure
    print ('''Try this TRY EXCEPT ELSE FINALLY Structure.\n
           Enter a string first.\n''')
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
    
    print ('''
        This structure enters a WHILE LOOP until a integer is entered. If an integer is entered the try, else, and finally branches activate.
        If a non-integer value is entered the loop will execute the EXCEPT branch and reprompt the user\n''')

def for_loops():
    print('''FOR LOOPS\n
        FOR LOOPS are a type of indefinate loop. They are used to do various tasks such as populating LISTS,
        completing a task in a set amount of iterations.
        FOR LOOPS require a PRIMING VALUE,and a Counter(INCRMENTOR OR DECREMENTOR)
        FOR LOOPS are often described as "for i in range of.." in classroom settings.\n''')
    
    proceed()
    
    #Create simple "for i in range of" FOR LOOP
    print("The following is a hardcoded simple FOR LOOP that prints number of iterations.\n")
    for i in range (3):
        print (i)

    proceed()
    
    print('''In the above example the you will see...\n
        0\n
        1\n
        2\n
        That is because all iterations start with 0 by defult in Python. Unless specified otherwise\n''')
    
    proceed()
    
    print('''RANGE CONTROL EXAMPLE/n
        To control range in a for loop, it can be declared as\nfor i in range (1, 4):\n''')
    for i in range (1,4):
        print(i)
    print("The RANGE CONTROL the above example starts at 1, and ALWAYS END AT THE HIGHEST DECLARED NUMBER - 1.\n")
    
    returnsToMAin()

def indefiniteLoops():
    print('''INDIFINITE LOOPS\n
          Indifinite loops are useful structures. They have a combo of a few components:\n
          1. Sentinel Value: A value that ends the loop.\n
          2. Flag: A bool that determines if an event has happened, I also call these switches.
          3. Counter: A structure that keeps counts of iterations, until it reaches the sentinel 
          3. Loop Body: the part of the loop that does the work\n
          4. Graceful exit: A way to exit the loop without breaking the program.\n
          The first example will be a an indefinite loop that relies of a sentinel value to exit\n
          sentinel_value = 4
          iteration_counter 0
          while sentinel_value > iteration_counter:
            print("Prints 4 times, because iterations in Python start with 0)
            iteration_counter += iteration counter
          print("Loop exited)\n''')
    
    proceed()
    
    # sentinel value exited indifinite loop. 
    sentinel_value = 4 # declare sentinel value
    iteration_counter = 0 # declare counter
    while sentinel_value > iteration_counter:
        print('This will print 4 times.')
        iteration_counter += 1 # increment counter at end of loop workflow
    print('Loop exited.\n') # stick the landing.

    proceed()
    
    print('''Next indefinite loop structure is what I call a flag loop.\n
          A flag loop uses a bool as a sentinel such that:
          counter = 0
          sentinel = False
          while sentinel == False:
            print(counter)
            if counter == 10:
                sentinel = True:
            else:
                sentinel = False
        print("Loop Exited")''')
    
    counter = 0 # set counter
    sentinel = False # set flag, True or False depending on what the usecase is.
    while sentinel == False:
        print(counter)
        counter += 1
        if counter == 10: # when counter hits the prescribed value, sentinel evaluates as True.
            sentinel = True
        else:
            sentinel = False # serves as a redundant switch
    print('Loop Exited.')

    returnsToMAin()

def functions():
    print('''FUNCTIONS\n
          When programming in any language it is important to not repeat yourself with repetative tasks.\n
          This is know as the "don't repeat youself" principal. (DRY).\n
          Functions are essential for completing repeatitive tasks. They can be used to call locations in a program,\n
          such as they are used in pythonCartographer, or to do repetative math operations.''')


main()     

 

