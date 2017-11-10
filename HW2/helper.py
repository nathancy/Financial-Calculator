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
        #print("For returning users, enter your username")
        #print("For new users, enter a new username and password")

        # Put all usernames into set 
        userset = set()
        with open('data.csv') as inputfile:
            csvfile = csv.reader(inputfile)
            next(csvfile)

            for line in csvfile:
                userset.add(line[0])
        
        # Check to see if username is in database
        username = input("Username: ")
        while (username not in userset):
            print("\"" + username + "\" is not registered. Please try again!")
            print("Please login as \"admin\" to add/remove users (Username: admin, Password: password)")
            username = input("Username: ")

        with open('data.csv') as inputfile:
            csvfile = csv.reader(inputfile)
            next(csvfile)
            
            #print("Username before check:", username)
            for line in csvfile:
                if username == line[0]:
                    #print("line[1] is:", line[1])
                    #print("Username found:", username)
                    #print("Checking password now")
                    password = input("Password: ")
                    #print("Entered password is:", password)
                    while password != line[1]:
                        #print("Entered password was is:", password)
                        print("Incorrect password, please try again!")
                        #print("line[1] is:", line[1])
                        password = input("Password: ")
                    return username

    # Print login successful information
    def afterLogin(self, username):
        print("+" * 60)
        print(" " * 12 + "Login successful!")
        print(" " * 12 + "Logged in as:", username)
        print("+" * 60)
    
    # Print selected currency information
    def currencySelected(self, currency_type):
        if currency_type == '1':
            print("Currency selected: USD")
        elif currency_type == '2':
            print("Currency selected: EURO")
        elif currency_type == '3':
            print("Currency selected: GBP")

