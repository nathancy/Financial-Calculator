import helper

helper = helper.Helper() 

helper.splashScreen()
username = helper.appLogin()
print("Returned username is:", username)

