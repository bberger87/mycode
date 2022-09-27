#!/usr/bin/env python3

num = 57
found =0
count =0

while found==0:
    guess = int(input("What's the magic numer? "))
    count += 1
    if num == guess:
        print("\nYour guess is correct the correct numer")
        found = 1
        break:
    elif guess in range(num-5,num):
        print("\nVery close but too low")
    elif num > guess:
        print("\nToo low")
    elif guess in range(num+1,num+5):
        print("\nVery close but too high")
    elif num < guess:
        print("\nToo high")
    print("\nGuess again")

print("\nTHank you")
print(f"Took you {count} guesses to find the correct number")
