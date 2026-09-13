from navigation import ATOPIC_Y_EXIT, PROCEED_CLASS, PROCEED_TO_MENU_CLASS, MENU_INPUT_HANDLER_CLASS

#TODO: fill read_write.py with content.

class READ_WRITE_MENU():

    @staticmethod
    def read_write_basics():
         print('Read write basics go here.')
         print('FIXME: fill content here. ')
         PROCEED_TO_MENU_CLASS.proceedToMenu()

    @staticmethod
    def run_read_write_menu():

        while True:
            
                # declarations for inputValidation() menu
                validation_menu =('''
                MENU - READ WRITE
                ........................................................................
                1: Input Read Write basics          
                OR ANY OTHER NUMBER TO EXIT.
                .........................................................................
                \n''')
            
                print(validation_menu)
                validation_selection = MENU_INPUT_HANDLER_CLASS.inputVald('Enter an integer to select a structure: \n')
    
                if validation_selection == 1:
                    ATOPIC_Y_EXIT.atopic
                    READ_WRITE_MENU.read_write_basics()
                else:
                    ATOPIC_Y_EXIT.exiting()
                    return