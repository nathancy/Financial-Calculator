import helper, commands, currency

helper = helper.Helper() 
commands = commands.Commands()
currency = currency.Currency()


helper.splashScreen()
username = helper.appLogin()
helper.afterLogin(username)

command = commands.getCommand()
if command == 'q':
    commands.commandExecute(command) 
while (command != 'q'):
    commands.commandExecute(command, username) 
    command = commands.getCommand()


