# Finnegan McGuire | Lab 7-4 |
# Purpose:

import random
import math
# Storage Variables
numbers = []

userInput = input("How many numbers will you generate? ")
userInput = int(userInput) - 1
while userInput >= 0:
    # Generate random number between 1 and 100
    rng = random.randrange(1, 100)

    total = 0
    total = total + rng
    numbers.append(str(rng))
    userInput = userInput - 1

numbers.sort()

smallestNumber = numbers.pop(0)
largestNumber = numbers.pop()
totalNumbersInList = len(numbers)
averageNumbers = []

print("Smallest Number: " + str(smallestNumber))
print("Largest Number: " + str(largestNumber))
print("Total Numbers In List: " + str(totalNumbersInList + 2))
print("Average Of All Numbers: ")