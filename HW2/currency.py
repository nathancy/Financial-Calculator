# Class to support currency conversions

import re, numbers, csv, os, helper
helper = helper.Helper()

EURO = 1.17 
GBP = 1.31

class Currency(object):
    # Ensure there is only one instance of Currency
    _instances=[]

    # Initialize the object
    def __init__(self):
        if (len(self._instances) > 1):
            print("ERROR: One instance of Currency is running already.")
            exit(1)
        self._instances.append(self)
   
    # Display current balance
    def balance(self, username):
        print("+" * 60)
        with open('data.csv', 'r') as inputfile:
            reader = csv.reader(inputfile)
            for row in reader:
                user, password, total, salt = row
                if user == username:
                    print("Current balance is: $" + str(total)) 
                    return str(total)
    
    # Withdraw currency from account
    def withdraw(self, username):
        print("+" * 60)
        print('''
            Currency types available to withdraw:

            1 - USD ($)
            2 - Euro (€)
            3 - GBP (£)
            ''')
        currency_type = str(input("Choose currency type to withdraw: "))
        # Get currency type (USD, Euro, or GBP)
        while (currency_type != '1' and currency_type != '2' and currency_type != '3'):
            print("+" * 60)
            print("Invalid currency type entered! Please try again.")
            print('''
            Currency types available to withdraw:

            1 - USD ($)
            2 - Euro (€)
            3 - GBP (£)
            ''')
            currency_type = str(input("Choose currency type to withdraw deposit: "))

        # Print selected currency message
        helper.currencySelected(currency_type)
        
        # Use regex to parse input and get amount
        amount = 0
        while (True):
            amount = input("Enter amount to withdraw: ")
            #print("Amount is:", amount)
            #print("Amount type is", type(amount))
            try:
                if '.' in amount:
                    amount = float(amount)
                else:
                    amount = int(amount)
                if (abs(float(self.currencyConverter(currency_type, amount))) > float(self.balance(username))):
                    print("You don't have enough funds! Please try again.")
                    continue;
                if (isinstance(amount, numbers.Real)):
                    break;
            except ValueError:
                print("+" * 60)
                print("Invalid withdraw amount entered! Please try again.")

        amount = str(amount) 
        #print("Amount after loop is:", amount)

        amount_regex = re.compile(r'(\d+(?:\.\d{1,2})?)')
        amount_pattern = amount_regex.search(amount)
        #print(amount_pattern.group())
        #print(type(amount_pattern.group()))
        amount = float(amount_pattern.group())
        #print("Final amount:", amount)
        original_amount = amount

        # Convert currency
        amount = self.currencyConverter(currency_type, amount)

        # Since we can't write to specific cell in csv, make new temporary csv without the current
        # user's information but save user's information. Then copy temporary csv into main csv again
        # Finally, append the new information since csv only allows append
        old_balance = ''
        old_password = ''
        salt_save= ''
        # Transfer real csv into temporary csv without user's information
        with open('data.csv', 'r') as inputfile:
            with open('data_new.csv', 'w') as outfile:
                reader = csv.reader(inputfile)
                writer = csv.writer(outfile)
                for row in reader:
                    user, hashed_password, total, salt = row
                    if username != row[0]:
                        field = [user, hashed_password, total, salt]
                        writer.writerow(field)
                    else:
                        old_balance = str(total)
                        old_password = str(hashed_password)
                        salt_save = salt
        # Overwrite real csv with temporary csv 
        with open('data_new.csv', 'r') as inputfile:
            with open('data.csv', 'w') as outfile:
                reader = csv.reader(inputfile)
                writer = csv.writer(outfile)
                for row in reader:
                    user, hashed_password, total, salt = row
                    field = [user, hashed_password, total, salt]
                    writer.writerow(field)
        # Append updated information into real csv
        with open('data.csv', 'a') as inputfile:
            writer = csv.writer(inputfile)
            new_balance = str((float(old_balance) - float(amount)))
            fields = [username, old_password, new_balance, salt_save]
            writer.writerow(fields)
        
        # Remove temporary csv file
        os.remove('data_new.csv')

        mode = 'withdraw'
        self.currencyExchangeRate(currency_type, str(original_amount), str(amount), mode)

    # Deposit currency into account
    def deposit(self, username):
        print("+" * 60)
        print('''
            Currency types available to deposit:

            1 - USD ($)
            2 - Euro (€)
            3 - GBP (£)
            ''')
        currency_type = str(input("Choose currency type to deposit: "))
        # Get currency type (USD, Euro, or GBP)
        while (currency_type != '1' and currency_type != '2' and currency_type != '3'):
            print("+" * 60)
            print("Invalid currency type entered! Please try again.")
            print('''
            Currency types available to deposit:

            1 - USD ($)
            2 - Euro (€)
            3 - GBP (£)
            ''')
            currency_type = str(input("Choose currency type to deposit: "))

        # Display currency selected
        helper.currencySelected(currency_type)
        
        # Use regex to parse input and get amount
        amount = 0
        while (True):
            amount = input("Enter amount to deposit: ")
            #print("Amount is:", amount)
            #print("Amount type is", type(amount))
            try:
                if '.' in amount:
                    amount = float(amount)
                else:
                    amount = int(amount)
                if (isinstance(amount, numbers.Real)):
                    break;
            except ValueError:
                print("+" * 60)
                print("Invalid deposit amount entered! Please try again.")

        amount = str(amount) 
        #print("Amount after loop is:", amount)

        amount_regex = re.compile(r'(\d+(?:\.\d{1,2})?)')
        amount_pattern = amount_regex.search(amount)
        #print(amount_pattern.group())
        #print(type(amount_pattern.group()))
        amount = float(amount_pattern.group())
        #print("Final amount:", amount)
        original_amount = amount

        # Convert currency
        amount = self.currencyConverter(currency_type, amount)

        # Since we can't write to specific cell in csv, make new temporary csv without the current
        # user's information but save user's information. Then copy temporary csv into main csv again
        # Finally, append the new information since csv only allows append
        old_balance = ''
        old_password = ''
        salt_save = ''
        # Transfer real csv into temporary csv without user's information
        with open('data.csv', 'r') as inputfile:
            with open('data_new.csv', 'w') as outfile:
                reader = csv.reader(inputfile)
                writer = csv.writer(outfile)
                for row in reader:
                    user, password, total, salt = row
                    if username != row[0]:
                        field = [user, password, total, salt]
                        writer.writerow(field)
                    else:
                        old_balance = str(total)
                        old_password = str(password)
                        salt_save = salt
        # Overwrite real csv with temporary csv 
        with open('data_new.csv', 'r') as inputfile:
            with open('data.csv', 'w') as outfile:
                reader = csv.reader(inputfile)
                writer = csv.writer(outfile)
                for row in reader:
                    user, password, total, salt = row
                    field = [user, password, total, salt]
                    writer.writerow(field)
        # Append updated information into real csv
        with open('data.csv', 'a') as inputfile:
            writer = csv.writer(inputfile)
            new_balance = str((float(old_balance) + float(amount)))
            fields = [username, old_password, new_balance, salt_save]
            writer.writerow(fields)
        
        # Remove temporary csv file
        os.remove('data_new.csv')
        
        mode = 'deposit'
        self.currencyExchangeRate(currency_type, str(original_amount), str(amount), mode)
            
    # Convert currency. 1 - USD, 2 - EURO, 3 - GBP
    def currencyConverter(self, currency_type, amount):
        if currency_type == '1':
            return amount
        elif currency_type == '2':
            return (float(amount) * float(EURO))
        elif currency_type == '3':
            return (float(amount) * float(GBP))
    
    # Print currency rates and deposit amount
    def currencyExchangeRate(self, currency_type, original_amount, final_amount, mode):
        if mode == 'deposit':
            print('''
            Current conversion rates:

            1 USD = 0.85 Euro
            1 USD = 0.77 GBP
            ''')
            print("+" * 60)
            if currency_type == '1':
                print("Successfully deposited $" + str(final_amount) + " into your account!") 
            elif currency_type == '2':
                print("Successfully deposited €" + str(original_amount) + " ($" + final_amount + ") into your account!") 
            elif currency_type == '3':
                print("Successfully deposited £" + str(original_amount) + " ($" + final_amount + ") into your account!") 
        elif mode == 'withdraw':
            print('''
            Current conversion rates:

            1 USD = 0.85 Euro
            1 USD = 0.77 GBP
            ''')
            print("+" * 60)
            if currency_type == '1':
                print("Successfully withdrew $" + str(final_amount) + " from your account!") 
            elif currency_type == '2':
                print("Successfully withdrew €" + str(original_amount) + " ($" + final_amount + ") from your account!") 
            elif currency_type == '3':
                print("Successfully withdrew £" + str(original_amount) + " ($" + final_amount + ") from your account!") 
                
