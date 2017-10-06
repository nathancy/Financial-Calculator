# Class to support currency conversions

import re, numbers, csv

class Currency(object):
    # Ensure there is only one instance of Currency
    _instances=[]

    # Initialize the object
    def __init__(self):
        if (len(self._instances) > 1):
            print("ERROR: One instance of Currency is running already.")
            exit(1)
        self._instances.append(self)
    
    def balance(self, username):
        print("hello")


    def deposit(self, username):
        print("+" * 60)
        print('''
            Currency types available to deposit:

            1 - USD ($)
            2 - Euro (€)
            3 - GBP (£)
            ''')
        currency_type = str(input("Choose currency type to deposit: "))
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

        print("Currency type is:", currency_type)   

        amount = 0
        while (True):
            amount = input("Enter amount to deposit: ")
            print("Amount is:", amount)
            print("Amount type is", type(amount))
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
        print("Amount after loop is:", amount)

        amount_regex = re.compile(r'(\d+(?:\.\d{1,2})?)')
        amount_pattern = amount_regex.search(amount)
        print(amount_pattern.group())
        print(type(amount_pattern.group()))
        amount = float(amount_pattern.group())
        print("Final amount:", amount)

        '''

                for row in reader:
                    username, password, total = row
                    if username == row[0]:
                        fields = [username, row[1], (float(row[2]) + float(amount))]
                        writer.writerow(fields)
        '''










        print("Deposited " + str(amount) + " into your account!") 
          
         

    
    def currencyConverter(self):
        print("test")
