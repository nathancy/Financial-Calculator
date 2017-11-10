# Class for all admin commands/interactions

import csv, os, random, hashlib

# String used to generate salt
ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" 

class Admin(object):
    # Ensure there is only one instance of Commands
    _instances=[]

    # Initialize the object
    def __init__(self):
        if (len(self._instances) > 1):
            print("ERROR: One instance of Commands is running already.")
            exit(1)
        self._instances.append(self)
    
    # Add user to database
    def addUser(self):
        # Put all usernames into set 
        userset = set()
        with open('data.csv') as inputfile:
            csvfile = csv.reader(inputfile)
            next(csvfile)
            
            for line in csvfile:
                userset.add(line[0])

        # Get new user's username
        new_user = input("Enter new user's username: ")
        while (new_user in userset):
            print("\"" + new_user + "\" is already registered. Please try again!")
            new_user = input("Enter new user's username: ")
        
        # Get new user's password
        new_password = input("Enter new password: ")
        
        # Generate salt
        salt = ''.join(random.choice(ALPHABET) for i in range(16))

        # Generate hashed_password using SHA512
        hashed_password = hashlib.sha512(str(new_password + salt).encode('utf-8')).hexdigest()

        # Add in the new username and hashed_password into database
        with open('data.csv', 'a') as inputfile:
            writer = csv.writer(inputfile)
            
            # Create .csv row with username, hashed password, set total to 0, and log salt
            fields = [new_user, hashed_password, 0, salt]
            writer.writerow(fields)

        print("\"" + new_user + "\" has been added to the database!")
        print("Default currency set to USD")

    # Remove user from database
    def removeUser(self):
        # Put all usernames into set to check if desired username exists
        userset = set()
        with open('data.csv') as inputfile:
            csvfile = csv.reader(inputfile)
            next(csvfile)
            
            for line in csvfile:
                userset.add(line[0])

        # Get username to delete 
        delete_user = input("Enter username to remove: ")
        while (delete_user not in userset):
            print("\"" + delete_user+ "\" is not in database. Please try again!")
            delete_user = input("Enter username to remove: ")
        
        # Since we can't edit cell in csv, make new temporary csv without the desired 
        # user to be deleted. Then copy temporary csv into main csv again

        # Transfer real csv into temporary csv without the desired user to be deleted
        with open('data.csv', 'r') as inputfile:
            with open('data_new.csv', 'w') as outfile:
                reader = csv.reader(inputfile)
                writer = csv.writer(outfile)
                for row in reader:
                    user, hashed_password, total, salt = row
                    if delete_user != row[0]:
                        field = [user, hashed_password, total, salt]
                        writer.writerow(field)

        # Overwrite real csv with temporary csv
        with open('data_new.csv', 'r') as inputfile:
            with open('data.csv', 'w') as outfile:
                reader = csv.reader(inputfile)
                writer = csv.writer(outfile)
                for row in reader:
                    user, hashed_password, total, salt = row
                    field = [user, hashed_password, total, salt]
                    writer.writerow(field)

        # Remove temporary csv file
        os.remove('data_new.csv')
        
        print("\"" + delete_user + "\" has been removed from the database!")
         
   
