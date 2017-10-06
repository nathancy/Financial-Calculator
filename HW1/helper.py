# Class to support login, splash screens, and standard output

import csv

class Helper(object):
    '''
    # Ensure there is only one instance of Helper 
    _instances=[]

    # Initialize the object
    def __init__(self):
        if (len(self._instances) > 1):
            print("ERROR: One instance of Helper is running already.")
            exit(1)
        self._instances.append(self)
    '''
    
    # Print splash screen
    def splashScreen(self):
        print("=" * 60)
        print("=" * 60)
        print(" " * 60)
        print(" " * 12 + "Welcome to the Financial Calculator!")
        print(" " * 60)
        print("=" * 60)
        print("=" * 60)

    # Control credential login
    # Validate password for existing user else create credentials for new user
    def appLogin(self):
        print("Please login with your credentials")
        print(" ")
        print("For returning users, enter your username")
        print("For new users, enter a new username and password")

        username = input("")
        
        with open('data.csv') as inputfile:
            
            csvfile = csv.reader(inputfile)
            next(csvfile)
            
            #print("Username before check:", username)
            for line in csvfile:
                if username == line[0]:
                    #print("line[1] is:", line[1])
                    #print("Username found:", username)
                    #print("Checking password now")
                    password = input("Enter password: ")
                    #print("Entered password is:", password)
                    while password != line[1]:
                        #print("Entered password was is:", password)
                        print("Incorrect password, please try again!")
                        #print("line[1] is:", line[1])
                        password = input("Enter password: ")
                    return username

            # If it gets here, it means its a new user not in the database
            new_password = input("Enter new password: ")
            with open('data.csv', 'a') as inputfile:
                writer = csv.writer(inputfile)

                # Create .csv row with username, password, and set total to 0
                fields = [username, new_password, 0]
                writer.writerow(fields)
                return username
    
    def afterLogin(self, username):
        print("+" * 60)
        print(" " * 12 + "Login successful!")
        print(" " * 12 + "Logged in as:", username)
        print("+" * 60)

    def currencySelected(self, currency_type):
        if currency_type == '1':
            print("Currency selected: USD")
        elif currency_type == '2':
            print("Currency selected: EURO")
        elif currency_type == '3':
            print("Currency selected: GBP")

