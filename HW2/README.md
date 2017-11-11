B
# Financial Calculator
The financial calculator keeps track of users, hashed passwords, salts, and the current balance. After logging into the application, available options are deposit, withdraw, transfer, view current balance, view users, help, and quit. The program uses regex to validate the input which will reject the user if invalid input is provided. The information for each user is stored in a .csv file. The application uses SHA512 encryption and a salt to ensure duplicate passwords are always unique.

In addition, only the 'admin' user is able to add and remove users from the database.

# Functions
- Add user
- Remove user
- List users
- Deposit
- Withdrawl
- Transfer
- View current balance

# Dependencies 
To run the application, you may need to install re, numbers, csv, random, hashlib, and os. The application was built using Python 3.6.1 but should work for any version of Python 3.X.X

To install dependencies: 
```
sudo apt-get install [package]
```

# Developers Guide
Run the application with:
```
python main.py
```

# Usage
For first time users, enter a new username and password. For returning users, the information is stored in the database and verifies hashed password credentials. After logging in, the user can deposit, withdraw, transfer, or view current balance. To deposit, choose currency type (USD, Euro, or GBP) then enter the amount to deposit. The conversion will be done automatically in the background. Similarly, to withdraw currency, select the currency type and enter the amount to withdraw. To transfer, a destination account is requested where the user can transfer funds from the source account. The user can also view the current balance in the account. Regex will validate currency inputs so it will keep retrying until correct input is given. 

# Examples
### Credential Login
![](docs/calculator1.png)

### Add user
![](docs/calculator4.png)

### Remove user
![](docs/calculator5.png)

### Deposit
![](docs/calculator2.png)

### Transfer 
![](docs/calculator6.png)

### Current Balance
![](docs/calculator3.png)
