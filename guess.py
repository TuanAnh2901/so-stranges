from random import randint as ri

n = ri(1, 100)

def inp(text):
    return int(input(text))

guess = inp("Guess the number between 1 and 100: ")
while True:
    if guess < n:
        print('\nToo low\n')
        guess = inp("Guess again: ")
    elif guess > n:
        print('\nToo high\n')
        guess = inp("Guess again: ")
    else:
        print ("\n\nYou got it!")
        break
