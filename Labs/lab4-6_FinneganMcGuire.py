# Lab 4-6: Temperature Conversion
# By: Finnegan McGuire
# Date Completed: February 17th, 2020

userInput_c = input("Enter a number to start with to convert into Fahrenheit: ")
userInput_f = input("Enter a number to end with to convert into Fahrenheit: ")
userInput_c = int(userInput_c)
userInput_f = int(userInput_f) + 1


print("Celsius To Fahrenheit Table")
print("----------------------------")
while userInput_c >= 0:
    f = userInput_c * 9/5 + 32
    print(str(userInput_c) + " C" + " ----> " + str(f) + " F")
    userInput_c = userInput_c + 1
    if userInput_c == userInput_f:
        break



