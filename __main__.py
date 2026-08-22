from navigation import MENU_INPUT_HANDLER_CLASS
from basics import BASICS_MENU
from inputs import INPUTS_MENU
from selections import SELECTION_MENU
from input_validation import INPUT_VALIDATION_MENU
from for_loops import FOR_LOOPS_MENU
from while_loops import WHILE_LOOP_MENU
from functions import FUNCTIONS_MENU
from lists import LISTS_MENU
from depopulate_list import DEPOPULATE_LIST_MENU
from dicts import DICTS_MENU


#TODO add regex section to input_validation
#TODO input_validation.py add exception hierarchy section
#TODO add file_operations.py and content
#TODO add slicing.py and content
#TODO add oop.py and content
#TODO add read_write.py and contents 

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
        6: WHILE LOOPS
        7: FUNCTIONS
        8: POPULATING LISTS
        9: DEPOPULATING LISTS
        10: DICTIONARIES
        OR ANY OTHER NUMBER TO EXIT.
        ------------------------------------------------------------------------
            ''')

        print(menu)

        select_structure = MENU_INPUT_HANDLER_CLASS.inputVald('Enter an integer to select a structure: \n')
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
            print('Accessing while loops...\n')
            WHILE_LOOP_MENU.runWhileLoopMenu()
        elif select_structure == 7:
            print('Accessing Functions...\n')
            FUNCTIONS_MENU.runFunctionsMenu()
        elif select_structure == 8:
            print('Accessing Populating Lists...\n')
            LISTS_MENU.runListsMenu()
        elif select_structure == 9:
            print('Accessing Depopulating Lists\n')
            DEPOPULATE_LIST_MENU.runDepopulateListMenu()
        elif select_structure == 10:
            print('Accessing Dictionaries\n')
            DICTS_MENU.runDictMenu()
        else:
            print('Exiting pythonCartographer!')
            break

# initiate pythonCartographer
if __name__ == '__main__':
    run()
    