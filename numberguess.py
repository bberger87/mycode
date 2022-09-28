#!/usr/bin/env python3

import random


def main():
    print("\n\nWelcome to The Random Number Guessing Game")
    print("\nA Random number gets generated between 1 and 100")
    print("and the user gets to guess until the correct number is chosen")
    num =  random.randint(1,100)
    count =0

    while True:
        guess = int(input("\nWhat is your guess for the number  ? "))
        count += 1
        if num == guess:
            print(f"\nCongratulations!!\n\nYour guess, {num}, is the correct number")
            print(f"\nIt took {count} guess(es) to find the correct number")
            break
        elif guess in range(num-5,num):
            print(f"\n{guess} is VERY close but LOW")
        elif num > guess:
            print(f"\n{guess} is TOO LOW")
        elif guess in range(num+1,num+5):
            print(f"\n{guess} is VERY close but HIGH")
        elif num < guess:
            print(f"\n{guess} is TOO HIGH")
        print("\nGuess again")

    print("\nThank you")
    print("To play again rerun the script again\n")


main()
