# Random Number Guessing Game (Lab 4-20)
# Created By: Finnegan McGuire
import math
import random

running = True
# Generate Random Number between 1 - 100


while running:
    rng = random.randint(1, 100)
    print("A random number has been created, try and guess the number!")
    guesses = 7
    print(f"You have {guesses} guesses")
    userGuess = input("Guess: ")
    userGuess = int(userGuess)

    while userGuess != rng:
        if userGuess > rng:
            print("Too High, Try Again!")
        if userGuess < rng:
            print("Too Low, Try Again!")

        print("Guesses Left: " + str(guesses))
        userGuess = input("Guess: ")
        userGuess = int(userGuess)
        guesses = guesses - 1
        if guesses <= 0:
            print("You ran out of guesses!")
            print("Game Over, reseting...")
            print("------------------")
            break
    if userGuess == rng:
        print("Correct!")
        print("Reseting...")
        break
