# Lab 3-19: Turtle Graphics: Hit The Target Modification
# By: Finnegan McGuire
# Date Completed: February 13th, 2020

import turtle

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
TARGET_LLEFT_X = 100
TARGET_LLEFT_Y = 250
TARGET_WIDTH = 25
FORCE_FACTOR = 30
PROJECTILE_SPEED = 1

# Directions
NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180

turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

#TARGET
turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(NORTH)
turtle.forward(TARGET_WIDTH)
turtle.setheading(SOUTH)
turtle.forward(TARGET_WIDTH)
turtle.penup()

#Center the turtle
turtle.goto(0, 0)
turtle.setheading(EAST)
turtle.showturtle()
turtle.speed(PROJECTILE_SPEED)

#UserInput
angle = float(input("Enter the projectile's angle: "))
force = float(input("Enter the launch force (1-10): "))

# Calculate the distance
distance = force * FORCE_FACTOR

#Set Heading
turtle.setheading(angle)

# Launch the projectile
turtle.pendown()
turtle.forward(distance)

target_position = "X: " + str(TARGET_LLEFT_X) + "Y: " + str(TARGET_LLEFT_Y)
print(target_position)
# did it hit the target?
if (TARGET_LLEFT_X <= turtle.xcor() <= (TARGET_LLEFT_X + TARGET_WIDTH) and
        turtle.ycor >= TARGET_LLEFT_Y and turtle.ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH)):
    print("Target Hit!")

# TASK: if user misses target recommend the user to increase/decrease the degrees.
else:
    print("Missed")

    if angle > 70.0168934542:
        print("Use less angle")
    if angle < 63.43494894947:
        print("Use more angle")
    if turtle.xcor() < 100 and turtle.ycor() < 250:
        print("Use more force")
    if turtle.xcor() < 125 and turtle.ycor() < 275:
        print("Use less force")

