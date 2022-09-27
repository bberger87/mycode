#!/usr/bin/env python3

secret num = 57

guess = int(input["What's the magic numer? "))

if secret_num == guess:
    print("Your guess is the correct the correct numer")

elif secret_num -2 < guess:
    print("Very close but too low")
elif secret_num < guess:
    print("Too low")
elif secret_num +2 > guess:
    print("Very close but too high")
elif secret_num > guess:
    print("Too high")
