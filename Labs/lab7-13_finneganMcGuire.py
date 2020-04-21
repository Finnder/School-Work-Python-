# Finnegan McGuire | Lab 7-13 |
# Purpose: The 8 ball program produces a random
# string of text by a random number generator
import random

userInput = input("Ask a Question: ")
rng = random.randrange(1, 8)

randomresponse = open("8_ball_responses.txt", "r")
Lines = randomresponse.readlines()

print(f"8-Ball: {Lines[rng]}")