#Input Password
def InputPassword(password):
    pas = input("Enter the passwords(Comma separated):")
    password = pas.split(',')
    return password


#Execution Starts Here
password = []
password = InputPassword(password)
ProcessPassword(password)

