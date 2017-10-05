# Class to support input commands 

class Commands(object):
    # Ensure there is only one instance of Commands
    _instances=[]

    # Initialize the object
    def __init__(self):
        if (len(self._instances) > 1):
            print("ERROR: One instance of Commands is running already.")
            exit(1)
        self._instances.append(self)
    
    # Print list of commands and return command
    def getCommand(self):
        command = input('''
            Commands:

            d - Deposit
            w - Withdrawl
            b - Balance 
            h - Help
            q - Quit

            ''')
        while (command != 'd' and command != 'w' and command != 'b' and command != 'h' and command != 'q'):
            print("+" * 60)
            print("Invalid command entered! Please try again.")
            command = input('''
            Commands:

            d - Deposit
            w - Withdrawl
            b - Balance 
            h - Help
            q - Quit

            ''')
            print(" ")
            return command
            
