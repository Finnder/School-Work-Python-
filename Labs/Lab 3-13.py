# Shipping Charges
# Name: Finnegan McGuire
# Date Created: 2/3/2020

userInput = input("Enter Pounds: ")
userInput = int(userInput)
print("User Entered: " + str(userInput))

if userInput <= 2:
    value = "1.50"
    print("$" + value)
if 2 < userInput < 6:
    value = "3.00"
    print("$" + value)
if 6 < userInput < 10:
    value = "4.00"
    print("$" + value)
if userInput > 10:
    value = "4.75"
    print("$" + value)


