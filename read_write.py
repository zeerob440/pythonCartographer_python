from navigation import ATOPIC_Y_EXIT, PROCEED_CLASS, PROCEED_TO_MENU_CLASS, MENU_INPUT_HANDLER_CLASS

#TODO: fill read_write.py with content.

class READ_WRITE_MENU():

    @staticmethod
    # basic skill overview for opening and reading/writing files
    def read_write_basics():

         print('''Read Write Basics

         Reading and writing files is and important skill set in Python.

         Reading files workflow is:
         1. open file example| with open('stringfilename.txt', 'Stringmode'):
         2. read file example| file_alias.read()
         3. close file example| use with open('filename.txt', 'mode') automatically closes file.
            otherwise file_alias.close()\n
         ''')

         PROCEED_CLASS.proceed()

         print('''READ WRITE OPEN MODES

         When opening a file you need to choose what mode to open it in. These modes are always strings.
         They include:
         open("file.txt", "r")    # Read existing file, cursor starts at beginning

         open("file.txt", "w")    # Erase file and write, because cursor starts at beginning

         open("file.txt", "a")    # Append only, writes always starts at end of file

         open("file.txt", "r+")   # Read/write existing file, cursor starts at beginning

         open("image.png", "rb")  # Read binary, cursor starts at beginning

         open("file.txt", "x")    # Create file only if it doesn't already exist\n''')

         PROCEED_TO_MENU_CLASS.proceedToMenu()

    @staticmethod
    # basic overview of read() and readlines()
    def read_readlines():

         print('''read() and readlines()

         Now that we have explained how to open files we will explore how to read them using hospital_quarantine.txt\n

         FOR SENIOR MANAGEMENT EYES ONLY

         San Cristobal Medical Facility Quarantine: active
         Entrance to Primary Care deck now limited to Marshals and Senior Staff.

         Universal facility pass code: 1702

         System will scan for potential quarantine breaches every fifteen (15) minutes.
         EOF\n
         ''')

         PROCEED_CLASS.proceed()

         print('''read()
         
         reads the entire files starting from cursor to EOF. we will uses this code to read the file.\n
         # using with open() open file in desired mode, give file an alias   
         with open('hospital_quarantine.txt', 'r') as read_file:
                         # assign a var to the file alias and .read()
                         read = read_file.read()
                         # data must be printed to display it.
                         print(read)
         proceed to run the code and read hospital_quarantine.txt!\n''')

         PROCEED_CLASS.proceed()
          
         with open('hospital_quarantine.txt', 'r') as read_file:
              read = read_file.read()
              print(read)

         PROCEED_CLASS.proceed()

         print('''read() can also take an integer arg. such as read(32). This means the program will read the 
         file from the cursor's current location to the number of char spaces as input as the arg, in this case, 31.
         
         let's try it. with this code.
         
         with open('hospital_quarantine.txt', 'r') as read_file:
                      read = read_file.read(32)
                      print(read)
         It will read the first 32 chars from cursor 0, and return 'FOR SENIOR MANAGEMENT EYES ONLY'
         Proceed to run it.\n''')

         PROCEED_CLASS.proceed()

         with open('hospital_quarantine.txt', 'r') as read_file:
                       read = read_file.read(32)
                       print(read)

         PROCEED_CLASS.proceed()

         print('''readlines() 
         
         readlines() is a function that reads the file into a list. It can also take an int agr to only read to a 
         certain place. so readlines(32) will only read 31 chars from the cursor.

         Here is the code we are working with:

         with open('hospital_quarantine.txt', 'r') as read_file_list:
                                read_list: list = read_file.readlines()
                                print(read_list)
         
         Let's try it on our hospital_quarantine.txt.''')

         PROCEED_CLASS.proceed()

         with open('hospital_quarantine.txt', 'r') as read_file_list:
                                         read_list: list = read_file_list.readlines()
                                         print(read_list)
         

         PROCEED_TO_MENU_CLASS.proceedToMenu()
         

    @staticmethod
    def run_read_write_menu():

        while True:
            
                # declarations for inputValidation() menu
                validation_menu =('''
                MENU - READ WRITE
                ........................................................................
                1: Input Read Write basics
                2: Read functions read(), readlines()          
                OR ANY OTHER NUMBER TO EXIT.
                .........................................................................
                \n''')
            
                print(validation_menu)
                validation_selection = MENU_INPUT_HANDLER_CLASS.inputVald('Enter an integer to select a structure: \n')
    
                if validation_selection == 1:
                    ATOPIC_Y_EXIT.atopic()
                    READ_WRITE_MENU.read_write_basics()
                elif validation_selection == 2:
                     ATOPIC_Y_EXIT.atopic()
                     READ_WRITE_MENU.read_readlines()
                else:
                    ATOPIC_Y_EXIT.exiting()
                    return