import helper, commands, currency

helper = helper.Helper() 
commands = commands.Commands()
currency = currency.Currency()

helper.splashScreen()
username = helper.appLogin()
helper.afterLogin(username)

commands.getCommand()

