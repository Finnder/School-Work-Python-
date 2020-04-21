# Lab 3-15: Time Calculator
# By: Finnegan McGuire
# Date Completed: February 9th, 2020

# User Input --> Float Number
timeInput = input("Enter Seconds To Be Converted: ")
print("Seconds Entered By User: " + str(timeInput))
time = float(timeInput)

# Math to convert Seconds into readable time
day = time // (24 * 3600)
time = time % (24 * 3600)
hour = time // 3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time

# Seconds --> ( Days | Hours : Min's : Secs )
print(f"{day} Days | {hour} Hr's: {minutes} Min's: {seconds} Sec's")
