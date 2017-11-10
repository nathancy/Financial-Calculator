# Class to support input commands 

import currency, helper, admin
currency = currency.Currency()
helper = helper.Helper()
admin = admin.Admin()

class Commands(object):
    # Ensure there is only one instance of Commands
    _instances=[]

    # Initialize the object
    def __init__(self):
        if (len(self._instances) > 1):
            print("ERROR: One instance of Commands is running already.")
            exit(1)
        self._instances.append(self)

    # (Admin user) Print list of commands and return command
    def getCommandAdmin(self):
        print("+" * 60)
        command = input('''
            Commands:
            
            a - Add User
            r - Remove User
            l - List Users
            d - Deposit
            w - Withdraw
            c - Current Balance 
            h - Help
            q - Quit

            ''')
        if command.isalpha(): 
            command = command.lower()
        while (command != 'd' and command != 'w' and command != 'c' and command != 'h' and command != 'q' and command != 'a' and command != 'r' and command != 'l'):
            print("+" * 60)
            print("Invalid command entered! Please try again.")
            command = input('''
            Commands:

            a - Add User
            r - Remove User
            l - List Users
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
    
    # (Normal user) Print list of commands and return command
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
        # Add user (ADMIN ONLY COMMAND)
        elif (command == 'a' and username == 'admin'):
            admin.addUser()
        # Remove user (ADMIN ONLY COMMAND)
        elif (command == 'r' and username == 'admin'):
            admin.removeUser()
        # List usernames in database (ADMIN ONLY COMMAND)
        elif (command == 'l' and username == 'admin'):
            admin.userList()
        # Deposit
        elif (command == 'd'):
            currency.deposit(username)
        # Current Balance
        elif (command == 'c'):
            currency.balance(username)
        # Withdraw 
        elif (command == 'w'):
            currency.withdraw(username)

