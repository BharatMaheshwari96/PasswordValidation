#Input Password
def InputPassword(password):
    pas = input("Enter the passwords(Comma separated):")
    password = pas.split(',')
    return password

#Process the passwords
def ProcessPassword(password):
    SpecialChar = ['$','#','@']
    Valid = []
    NotValid = []
    for i in range(len(password)):
        FlagLen = 0
        FlagDig = 0
        FlagUpr = 0
        FlagLow = 0
        FlagSpe = 0
        if ((len(password[i]) > 6) and (len(password[i]) < 12)):
            FlagLen = 1
        for ch in password[i]:
            if(ch in SpecialChar):
                FlagSpe = 1
            if(ch.isdigit()):
                FlagDig = 1
            if(ch.isupper()):
                FlagUpr = 1
            if(ch.islower()):
                FlagLow = 1

        if(FlagLen ==1 and FlagSpe == 1 and FlagDig ==1 and FlagUpr == 1 and FlagLow ==1):
            Valid.append(password[i])
        else:
            NotValid.append(password[i])

    print("The following passwords do NOT meet the criteria:\n")
    print(NotValid)
    print("The following passwords meet the criteria:\n")
    print(Valid)



#Execution Starts Here
password = []
password = InputPassword(password)
ProcessPassword(password)

