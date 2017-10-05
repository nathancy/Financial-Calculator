# Class to support currency conversions

class Currency(object):
    # Ensure there is only one instance of Currency
    _instances=[]

    # Initialize the object
    def __init__(self):
        if (len(self._instances) > 1):
            print("ERROR: One instance of Currency is running already.")
            exit(1)
        self._instances.append(self)
    
    def currencyConverter(self):
        print("test")
