'''
navigation.py contains class methods that enable the user to navigate the application. 
'''

class PROCEED_CLASS():
    # It asks the user to continue after each example within a lesson.
    @staticmethod
    def proceed():
        any_key_to_continue = input('''\n
            Press any key to proceed.\n''')

class PROCEED_TO_MENU_CLASS():
    @staticmethod
    def proceedToMenu():
        any_key_to_menu = input('''\n
                This concludes this module. Press any key to continue.\n''')
    
# Used to denote that content is being accessed, informs user when exiting.
class ATOPIC_Y_EXIT():
    @staticmethod
    def atopic():
        statement = 'Accessing Topic...\n'
        print(statement)

    #ex used to declare that a menu is exiting.
    @staticmethod 
    def exiting():
        ex = 'Exiting...\n'
        print(ex)
        # returns to previous program
        return

    
    # improved input handling class
    '''This function obtains user input, converts it to an integer if it isdigit() and returns that integer value,
    otherwise it will prompt the user to input an integer. This class is part of the pythonCartographer Delta refactor that improved input handling.'''
class MENU_INPUT_HANDLER_CLASS:

    @staticmethod
    def inputVald(prompt):
        while True:
            selection = input(prompt)
            if selection.isdigit():
                selection = int(selection)
                return selection
            else:
                print('Enter an integer!\n')

