# Class to support input commands 

import currency, helper
currency = currency.Currency()
helper = helper.Helper()

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
        print("+" * 60)
        command = input('''
            Commands:

            d - Deposit
            w - Withdraw
            c - Current Balance 
            h - Help
            q - Quit

            ''')
        if command.isalpha(): 
            command = command.lower()
        while (command != 'd' and command != 'w' and command != 'c' and command != 'h' and command != 'q'):
            print("+" * 60)
            print("Invalid command entered! Please try again.")
            command = input('''
            Commands:

            d - Deposit
            w - Withdraw
            c - Current Balance 
            h - Help
            q - Quit

            ''')
            if command.isalpha(): 
                command = command.lower()
            print(" ")
        return command
   
    # Execute the given command 
    def commandExecute(self, command, username):
        # Quit
        if (command == 'q'):
            print("Exiting financial calculator")
            exit(1)
        # Deposit
        elif (command == 'd'):
            currency.deposit(username)
        # Current Balance
        elif (command == 'c'):
            currency.balance(username)
        # Withdraw 
        elif (command == 'w'):
            currency.withdraw(username)

