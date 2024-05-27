


def daysToUnits(numberOfDays):
    if numberOfDays > 0:
        return f" Number of hours in days are {60 * numberOfDays}"
    else:
        return "you enterd a negative value !"
    

def validateAndExcute():
    try:
        userInputAsNumber = int(userInput)
        if userInputAsNumber > 0:
                calculatedValue = daysToUnits(userInputAsNumber)
                print(calculatedValue)
        elif userInputAsNumber == 0:
                print('check the value it is equal to zero')
    except ValueError:
        print('your input is not a valid number !')          
userInput =  ""
while(userInput != 'exit'):
     userInput = input("input the number of days !\n")
     validateAndExcute()       




    

