import random

try:
    n = random.randrange(1,100)
    guess = int(input("Enter any number: "))
    while n!= guess:
        if guess < n:
            print("Too low")
            guess = int(input("Enter number again: "))
        elif guess > n:
            print("Too high!")
            guess = int(input("Enter number again: "))
        else:
            print("you guessed it right!!")
            break
except:
    print("please number")