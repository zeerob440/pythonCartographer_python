from navigation import ATOPIC_Y_EXIT, PROCEED_CLASS, PROCEED_TO_MENU_CLASS

# functions.py provides example of function behaviors.
class FUNCTIONS_MENU():

    @staticmethod
    def functionBasics():
        print('''
        FUNCTIONS\n
        When programming in any language it is important to not repeat yourself with repetitive tasks.
        This is know as the "don't repeat yourself" principal. (DRY).
        Functions are essential for completing repetitive tasks. They can be used to invoke locations in a program,
        such as the way they are used in pythonCartographer, or to do repetitive tasks.\n.
        
        Functions are special because they can return values from the function to the program that invoked it.\n''')

        PROCEED_CLASS.proceed()

        print('''STRUCTURE OF A FUNCTION\n
        1 PARAMETERS - def fun(a, b): WHERE a, b are parameters OR what values the function expects to process.\n''')

        PROCEED_CLASS.proceed()

        print('''2 ARGUMENTS - are values passed to parameters such that:\n
        a = 5 # 5 is the arg for parameter 'a'
        b = 10 # 10 is the arg for parameter 'b'
        def fun(a, b):
            # here a = 5 and b = 10, the arguments.\n''')

        PROCEED_CLASS.proceed()

        print('''3 RETURNS - The value a function returns after processing arguments. return always
        returns args to the area of the program that invoked the function such that:

        def fun(a, b):
            result = a + b
            return result
        # store function as var in return area, print var.
        value = fun(5,10)
        
        print(value))\n''')

        PROCEED_CLASS.proceed()

        print('Functions can be relatively simple or complex as a result.\n')
        
        PROCEED_TO_MENU_CLASS.proceedToMenu()

    @staticmethod
    def declarParam():

        print(''' 
        DECLARING PARAMETERS\n
        Functions process arguments. In order for a function to process an argument parameters must
        be set in the function declaration. Positional parameters can be used.\n
        itAddsThings(a, b)
        result = a + b
        return result\n
        Below you will run this code. It will add args you provide and return the sum.\n''')

        PROCEED_CLASS.proceed()

        def itAddsThings(a, b):
            result = a + b
            return result

        while True:
            a = input('Enter an integer: ')
            b = input('Enter another integer: ')
            if a.isdigit() and b.isdigit():
                a = int(a)
                b = int(b)
                answer = itAddsThings(a, b)
                break
            else: continue

        print(f'The args pass through the parameters added together = {answer}\n')

        PROCEED_TO_MENU_CLASS.proceedToMenu()
            
    @staticmethod
    def keyWordPrams():

        print('''DEFAULT PARAMETERS\n
        default parameters are parameters set with default values such that:\n

        def itAddsDF(d = 7 , f = 3): # function is declared with default parameters
                    added = d + f   # store value
                    return added\n

        print(itAddsDF()) # prints 10, parameters NOT required in the invocation.\n

        will print 10 because not args have been passed into the function.\n

        Let's try it!\n''')
    
        PROCEED_CLASS.proceed()

        
        def itAddsDF(d =7 , f = 3): # function is declared with default parameters
            added = d + f
            return added
        
        print(f'function printed the sum of the default parameters which is: {itAddsDF()}\n')

        print('''Keyword args can also override default parameters such that:\n
        print(itAddsDF(f = 10))\n
        this allows the 0th parameter to remain the default but explicitly changes the second
        parameter to 10 with a keyword arg.
        let's try it!\n''')

        PROCEED_CLASS.proceed()

        print(f'This function has returned {itAddsDF(f = 10)}, since d = 7 and f has been changed to 10.\n') # prints 17

        PROCEED_TO_MENU_CLASS.proceedToMenu()

    @staticmethod
    def packUPack():
        print('''PACKING AND UNPACKING RETURNS BETWEEN PROGRAMS OR SCOPE.\n
        Functions are often used such that one program obtains args, then invokes a separate program to with a 
        function to process the args. To do this args must be packed and unpacked.\n
        
         while True:
                    h_in = input('Enter integer for h: ')\n
                    i_in = input('Enter integer for i: ')\n
                    j_in = input(' Enter integer for j: ')\n
                    if h_in.isdigit() and i_in.isdigit() and j_in.isdigit():
                        # convert to int.
                        h = int(h_in)
                        i = int(i_in)
                        j = int(j_in)
                        break
        
                def itReturnsThree(h, i, j):
                    hh = h + h
                    ii = i * i
                    jj = j ** j
        
                    return hh, ii, jj
        
                # unpack structure below
                # outside of function scope
                # it unpacks on the left and is invoked while taking arguments on the right.
                hh, ii, jj = itReturnsThree(h, i, j)
        
                print(h, i, j are passed into the function. The function lives the first nesting level, it
                returns hh, ii , jj to the 0th nesting level. The returns are unpacked, and then printed.)
                print(f'h + h = {hh}')
                print(f' i * i = {ii}')
                print(f'j ** j = {jj}''')

        print("Let's run it.\n")

        PROCEED_CLASS.proceed()

        while True:
            h_in = input('Enter integer for h: \n')
            i_in = input('Enter integer for i: \n')
            j_in = input(' Enter integer for j: \n')
            if h_in.isdigit() and i_in.isdigit() and j_in.isdigit():
                # convert to int.
                h = int(h_in)
                i = int(i_in)
                j = int(j_in)
                break

        def itReturnsThree(h, i, j):
            hh = h + h
            ii = i * i
            jj = j ** j

            return hh, ii, jj

        # unpack structure below
        # outside of function scope
        # it unpacks on the left and is invoked while taking arguments on the right.
        hh, ii, jj = itReturnsThree(h, i, j)

        print('''h, i, j are passed into the function. The function lives the first nesting level, it
        returns hh, ii , jj to the 0th nesting level. The returns are unpacked, and then printed.\n''')
        print(f'h + h = {hh}')
        print(f'i * i = {ii}')
        print(f'j ** j = {jj}')

        PROCEED_CLASS.proceed()

    @staticmethod
    def positionalArgs():  

        print('''POSITIONAL ARGUMENTS\n
        
        Positional arguments are args that can be passed by position. Consider:\n
        def posEx(g = 2, h = 3):
            sumGH = g + h
            return sumGH\n
        print(posEX()) # prints 5
        Default parameters are provided, so the function will always return 5 when invoked without args.
        Let's try it\n''')

        PROCEED_CLASS.proceed()

        def posEx(g = 2, h = 3):
                sumGH = g + h
                return sumGH
        
        print(f'The function has printed: {posEx()}\n') # prints 5

        PROCEED_CLASS.proceed()

        print('''Now let's override default parameters using positional arguments.\n
        print(posEx(5)) # returns 8\n

        print(posEx(2,2)) # returns 4
        
        This will assign 5 to the 0th parameter and leave the 1st parameter's default value.
        let's try it.\n''')

        PROCEED_CLASS.proceed()

        print(f'posEX(f) is: {posEx(5)}\n') # returns 8

        print(f'posEx(2, 2) is: {posEx(2,2)}.\n')

        
        PROCEED_TO_MENU_CLASS.proceedToMenu()

    @staticmethod
    def lambdaFun():
            print('''lambda are small quick functions, they are structured as:
            name = lambda parameters: return_value
            
            We'll examine how a traditional function looks when written as a lambda\n
            def shout(name):
                            return name.upper()
            
                        print(shout("rico"))

            Can be written as:\n
             shout = lambda name: name.upper()
            
                        print(shout("rico"))

            each function outputs 'RICO'.
            Now let's try them!
            ''')
            PROCEED_CLASS.proceed()

            # lambda functions
            # structure
            # name = lambda parameters: return_value
            print('Trad function output below:\n')
            # traditional function
            def shout(name):
                return name.upper()

            print(shout("rico"))

            print('Proceed to produce above output with lambda.\n')

            PROCEED_CLASS.proceed()

            print('lambda output function below\n')
            # equal lambda function, args, if any go next to lambda followed by a : it can take 0 - inf args
            shout = lambda name: name.upper()

            print(shout("rico"))

            PROCEED_CLASS.proceed()

           
            double = lambda x: x * 2

            print(double(2))
            print('''lambda functions can take as many parameters as needed. The parameters are separated by ","
                lambda can have default parameters, or positional parameters\n
                However, params without defaults MUST be declared BEFORE Default params such that:\n
                
                triple_10 = lambda x2, x10=5: (x2 * 3, x10 * 10)
            
                print(triple_10(3))# prints 59\n
                
                proceed to run this code.\n''')

            PROCEED_CLASS.proceed()
            
            triple_10 = lambda x2, x10=5: (x2 * 3, x10 * 10)

            print(f'The default param lambda is: {triple_10(3)}')# prints 59

            PROCEED_CLASS.proceed()

            print('''map() FUNCTION\n
            
            lambda functions are especially useful with the map() and filter() function\n
            structure: map(function, iterable)
            takes a function and adds the result to an iterable
            map creates generator object, it must be extracted with an iterable.\n
            Let's check out this code\n
            
            dogs =['mia', 'rico', 'orion']
            
                result = map(lambda dog: dog.upper(), dogs)
                # object extracted as list. 
                print (list((result)))\n

            proceed to run the code\n''')
            # map()
            # map(function, iterable)
            # takes a function and adds the result to an iterable
            # map creates generator object, it must be extracted with an iterable. 
            dogs =['mia', 'rico', 'orion']

            result = map(lambda dog: dog.upper(), dogs)

            # object extracted as list. 
            print (list((result)))

            PROCEED_CLASS.proceed()

            print('''filter() FUNCTION\n
            filter() filters things from an iterable and returns those that meet criteria to a list.
            structure filter(function, iterable)
            
            result must must be extracted with an iterable\n
            def dogFilter(dog):
                            return len(dog) == 4
                        
                        # unpack function
                        fun_result = list(filter(dogFilter, dogs))
                        print(fun_result)
            
                        f_result = list(filter(lambda dog: len(dog) == 4, dogs))
            
                        print(f_result)\n
            proceed to try this code, it will return 'rico'. ''')

            # filter()
            # filter(function, iterable)
            # creates a generator-object that must be extracted with an iterable

            PROCEED_CLASS.proceed()

            def dogFilter(dog):
                return len(dog) == 4
            
            # unpack function
            fun_result = list(filter(dogFilter, dogs))
            print(fun_result)

            f_result = list(filter(lambda dog: len(dog) == 4, dogs))

            print(f_result, end='\n')

            print('This concludes this module.\n')

            PROCEED_TO_MENU_CLASS.proceedToMenu()


    # This lesson is longer because it reuses the same code throughout the lesson.
    @staticmethod   
    def intermediateFunctionOps():

        print('''OUTPUT RETURNS\n
            Producing output for returns follows this process:\n
            1. Declare Vars needed for function arguments
            2. Declare Functions.
            3. Invoke functions.
            4. Save returns to variables in the main program.
            ''')
        
        PROCEED_CLASS.proceed()
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

        PROCEED_CLASS.proceed()

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


        PROCEED_CLASS.proceed()
    
    
        print('''OUTPUT FUNCTION WITH f-STRING\n
        It is possible to print a function to an f-string by:\n
        print(f'a + b = {itAddsThings(a, b)}')\n
        print(f'a - b = {itSubtractsThings(a, b)}')
        print(f'a * b = {itMultipliesThings(a, b)}')\n
        print(f'a / b = {itDividesThings(a, b)}')\n  
        Proceed to see the values output in f-strings.\n
        ''')
    
        PROCEED_CLASS.proceed()

        # printing functions to f-string is possible.
        print(f'a + b = {itAddsThings(a, b)}\n')
        print(f'a - b = {itSubtractsThings(a, b)}\n')
        print(f'a * b = {itMultipliesThings(a, b)}\n')
        print(f'a / b = {itDividesThings(a, b)}\n')

        PROCEED_CLASS.proceed()

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

        PROCEED_CLASS.proceed()

        # function return values can be used to create new variables and print statements.
        print(itMultipliesThings(a, b) + 9)
        divide_multiply_sum = (itDividesThings(a, b) + itMultipliesThings(a, b))
        print(divide_multiply_sum)

        PROCEED_CLASS.proceed()

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

        PROCEED_CLASS.proceed()

        divide_multiply_sum = (itDividesThings(a, b) + itMultipliesThings(a, b))

        add_subtract_sum = (itAddsThings(a,b) + itSubtractsThings(a, b))

        print(add_subtract_sum)

        print(divide_multiply_sum)

        # using itAddsThings function with new args to add divide_multiply_sum and add_subtract_sum
        itAddsThings(divide_multiply_sum, add_subtract_sum)

        print(f'''
        The new args in itAddsThings(divide_multiply_sum, add_subtract_sum)
        is:{itAddsThings(divide_multiply_sum, add_subtract_sum)}.\n''')


        PROCEED_TO_MENU_CLASS.proceedToMenu()

    def runFunctionsMenu():    
        while True:
        
            # declarations for functions() menu
            functions_menu =('''
            MENU - Functions
            ........................................................................
            1: Functions Basics
            2: Declaring Parameters
            3: Keyword Parameters
            4: Positional Arguments
            5: Packing & Unpacking Functions
            6: Lambda Functions
            7: Intermediate Functions Operations           
            OR ANY OTHER NUMBER TO EXIT.
            .........................................................................
            \n''')
        
            print(functions_menu)
            functions_selection = int(input('Select a Topic \n'))

            if functions_selection == 1:
                ATOPIC_Y_EXIT.atopic()
                FUNCTIONS_MENU.functionBasics()
            elif functions_selection == 2:
                ATOPIC_Y_EXIT.atopic()
                FUNCTIONS_MENU.declarParam()
            elif functions_selection == 3:
                ATOPIC_Y_EXIT.atopic()
                FUNCTIONS_MENU.keyWordPrams()
            elif functions_selection == 4:
                ATOPIC_Y_EXIT.atopic()
                FUNCTIONS_MENU.positionalArgs()
            elif functions_selection == 5:
                ATOPIC_Y_EXIT.atopic()
                FUNCTIONS_MENU.packUPack()
            elif functions_selection == 6:
                FUNCTIONS_MENU.lambdaFun()
            elif functions_selection == 7:
                FUNCTIONS_MENU.intermediateFunctionOps()
            else:
                ATOPIC_Y_EXIT.exiting()
                return    