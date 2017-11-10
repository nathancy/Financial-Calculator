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

# Get user or admin commands
if username == "admin":
    command = commands.getCommandAdmin()
else:
    command = commands.getCommand()

# User quits right after login
if command == 'q':
    commands.commandExecute(command, username)
while (command != 'q'):
    # Admin prompt
    if username == "admin":
        commands.commandExecute(command, username)
        command = commands.getCommandAdmin()
    # Regular user prompt
    else:
        commands.commandExecute(command, username) 
        command = commands.getCommand()
print("Exiting financial calculator")
