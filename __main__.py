from basics import BASICS_MENU
from inputs import INPUTS_MENU
from selections import SELECTION_MENU
from input_validation import INPUT_VALIDATION_MENU
from for_loops import FOR_LOOPS_MENU


'''
Version: Delta 6 AUG 2026; pythonCartographer Delta was created to make the program more modular and easier to maintain. 
This program uses OOP concepts to navigate learning modules. 
   
Proudly engineered by Zachary Roberts 11 August, 2025 
"We should now have access to the main facility. Let's find the map room."-Cortana
'''

print ("This program helps navigate notes and simple structures in the Python language. Zachary Roberts 11 AUG 2025.\n")

# Start Program
def run():
    
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
            BASICS_MENU.runBasicsMenu()
        elif select_structure == 2:
            print ("Accessing Inputs...\n")
            INPUTS_MENU.runInputsMenu()
        elif select_structure == 3:
            print ("Accessing Selections...\n")
            SELECTION_MENU.runSelectionsMenu()
        elif select_structure == 4:
            print ("Accessing Input Validation...\n")
            INPUT_VALIDATION_MENU.runInputValidationMenu()
        elif select_structure == 5:
            print("Accessing For Loops...\n")
            FOR_LOOPS_MENU.runForLoopMenu()
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

# initiate pythonCartographer
if __name__ == '__main__':
    run()
    