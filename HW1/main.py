# Main driver for financial calculator
import helper, commands, currency

# Instantiate objects
helper = helper.Helper() 
commands = commands.Commands()
currency = currency.Currency()

# Display splash screen 
helper.splashScreen()

# Verify password and username login
username = helper.appLogin()

# Print successful credential login
helper.afterLogin(username)

# Get user commands
command = commands.getCommand()
if command == 'q':
    commands.commandExecute(command) 
while (command != 'q'):
    commands.commandExecute(command, username) 
    command = commands.getCommand()

