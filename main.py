import functions

def whatever ():
    print("hello world")
whatever()
##########################################
userInput =  ""
while(userInput != 'exit'):
     userInput = input("input the number of days !\n")
     for x in userInput.split():
          functions.validateAndExcute(x)

