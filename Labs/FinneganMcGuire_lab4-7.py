# Lab 4-7: Pennies For pay


userDays = input("Enter days: ")
userDays = int(userDays)
pennies = 0.01
days = 0
totalEarned = 0

while days < userDays:
    days += 1
    print("Day:" + str(days) + " | $" + str(pennies))
    totalEarned += pennies
    pennies *= 2

print("-----------------------")
print("Total Amount Earned: " + "$ " + str(totalEarned))






