

def daysToUnits(numberOfDays):
    if numberOfDays > 0:
        return f" Number of hours in days are {60 * numberOfDays}"
    else:
        return "you enterd a negative value !"
    
userInput = input("input the number of days !\n")
userInputAsNumber = int(userInput)
calculatedValue = daysToUnits(userInputAsNumber)

print(calculatedValue)