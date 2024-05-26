

def daysToUnits(numberOfDays):
    return f" Number of hours in days are {60 * numberOfDays}"

userInput = input("input the number of days !\n")
userInputAsNumber = int(userInput)
calculatedValue = daysToUnits(userInputAsNumber)

print(calculatedValue)